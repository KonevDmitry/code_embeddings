import ast
from ast import parse
import json
import csv
import parse_python as pp
import gzip
import os
import jsonlines


def add_ast(ast_tree):
    with open('output.json', mode='a', encoding='UTF-8') as writer:
        if ast_tree is not None:
            writer.write(ast_tree)
            writer.write("\n")


def run(str, file):
    res = pp.parse_file(str)
    add_ast(res)

def parse(json_file):
    with open(json_file) as f:
        for line in f:
            data = json.loads(line)
            data_code = data['original_string']
            run(data_code, "./test_file.py")

def read_data():
    # folder = os.getcwd()+"\\python_data\\python\\final\\jsonl\\test\\python_test_0.jsonl.gz"
    # with gzip.open(folder, "rb") as f:
    #     data = f.read().decode("utf-8")
    #     #     run(data)
    file = os.getcwd() + "\\python_test_0.jsonl\\python_test_0.jsonl"
    parse(file)
    # run(file)
if __name__ == '__main__':
    # create_csv()
    read_data()
    # print(run("./test_file.py"))