import ast
import glob
import json
import os
import sys
import tqdm

from elasticsearch import Elasticsearch


def read_file(input_dir):
    filenames = glob.glob(input_dir + f"/*train*")
    for i in range(len(filenames)):
        with open(f"{input_dir}/python_train_{i}.jsonl") as infile, open(f"{input_dir}/pred.txt") as pred:
            for line,pred_line in zip(infile,pred):
                js = json.loads(line)
                try:
                    ast.parse(js['code'])
                except SyntaxError:
                    continue
                js.update({"pred":pred_line[:-1]})
                es.index(index="python", doc_type="func", body=js)
        print(f"{input_dir}/python_train_{i}.jsonl")

def read_files(path):
    files = glob.glob(path)
    for file in files:
        read_file(file)

if __name__ == '__main__':
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    path = "../resources/input" if len(sys.argv)<2 else sys.argv[1]
    read_files(path)