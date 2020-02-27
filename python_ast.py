import json
import parse_python as pp
import os


def save_ast(ast_tree, out_path):
    os.makedirs(out_path[:out_path.rfind("/")], exist_ok=True)
    with open(out_path, mode='a', encoding='UTF-8') as writer:
        if ast_tree is not None:
            writer.write(ast_tree)
            writer.write("\n")


def run(str, out_path):
    save_ast(pp.parse_file(str), out_path)


def parse(json_file, out_dir):
    with open(json_file) as f:
        for line in f:
            data = json.loads(line)
            data_code = data['original_string']
            run(data_code, out_dir)


def read_data(inp_dir, out_dir):
    files = os.listdir(inp_dir)
    for file in files:
        parse(inp_dir + "/" + file, out_dir)


if __name__ == '__main__':
    read_data("./input", "./past_res/result.json")
