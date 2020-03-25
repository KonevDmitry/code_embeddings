import glob
import json
import os
import sys
import tqdm

from elasticsearch import Elasticsearch


def read_file(file):
    with open(file, "r") as f:
        for i in tqdm.tqdm(f.readlines()):
            es.index(index="python",doc_type="func", body=json.loads(i))
        print("file")

def read_files(path):
    files = glob.glob(path)
    for file in files:
        read_file(file)

if __name__ == '__main__':
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    path = "../resources/python/python/final/jsonl/train/*.jsonl" if len(sys.argv)<2 else sys.argv[1]
    read_files(path)