import threading

from flask import Flask
from flask import render_template
from flask import request
from elasticsearch import Elasticsearch
import fulltext.search
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        docs = fulltext.search.search_python(es, request.args.get('query'))
        return render_template('results.html', docs=docs)
    return 'smt'

@app.route('/get_doc', methods=['GET'])
def get_doc():
    if request.method == 'GET':
        return render_template('doc.html', doc=search.get_doc())
    return 'smt'


@app.route('/')
def hello_world(name=None):
    return render_template('main.html', name=name)


# @app.route("/new_doc", methods=['GET', 'POST'])
# def new_doc():
#     if request.method == 'GET':
#         return render_template("new_doc.html")
#     elif request.method == "POST":
#         engine_obj.update(request.form['text'])
#         return render_template("main.html", name=None)



if __name__ == '__main__':
    app.run()