import json

import unidecode as unidecode
from multiprocessing import Process
import parse_python as pp
import os
import csv
import tqdm


def save_ast(ast_tree, out_path):
    os.makedirs(out_path[:out_path.rfind("/")], exist_ok=True)
    with open(out_path, mode='a', errors='surrogatepass') as writer:
        if ast_tree is not None:
            writer.write(ast_tree)
            writer.write("\n")

def run(str, out_path):
    save_ast(pp.parse_file(str), out_path)


def parse(json_file, out_dir):
    with open(json_file) as f:
        for line in tqdm.tqdm(f):
            data = json.loads(line)
            data_code = data['original_string']
            run(data_code, out_dir)


def parse_csv(json_file, out_dir):
    with open(json_file, 'r', newline='', errors="replace") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for data in tqdm.tqdm(spamreader):
            data_code = data[2]
            run(data_code, out_dir)


def read_data(inp_dir, out_dir):
    files = os.listdir(inp_dir)
    procs = []
    for file in files:
        if file.split(".")[1] == 'jsonl':
            pr = Process(target=parse, args=(inp_dir + "/" + file, out_dir+"/"+file))
        else:
            pr = Process(target=parse_csv, args=(inp_dir + "/" + file, out_dir+"/"+file))
        pr.start()
        procs.append(pr)
    for proc in procs:
        proc.join()


if __name__ == '__main__':
    read_data("./input", "./past_res")
