import json
import threading

from flask import Flask
from flask import render_template
from flask import request
from elasticsearch import Elasticsearch
import fulltext.search
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

app = Flask(__name__)
ast = True
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        global ast
        docs = fulltext.search.search_python(es,ast, request.args.get('query'))
        return render_template('results.html', docs=docs)
    return 'smt'

@app.route('/get_doc', methods=['GET'])
def get_doc():
    if request.method == 'GET':
        return render_template('doc.html', doc=fulltext.search.get_doc(es, request.args.get("docid")))
    return 'smt'

@app.route('/change_searcher', methods=['GET'])
def change_searcher(name=None):
    if request.method == 'GET':
        global ast
        ast = not ast
        return render_template('main.html', name=name, ast=ast)
    return 'smt'


@app.route('/')
def main_page(name=None):
    return render_template('main.html', name=name, ast=ast)


# @app.route("/new_doc", methods=['GET', 'POST'])
# def new_doc():
#     if request.method == 'GET':
#         return render_template("new_doc.html")
#     elif request.method == "POST":
#         engine_obj.update(request.form['text'])
#         return render_template("main.html", name=None)



if __name__ == '__main__':
    app.run()