import glob
import json
import os
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        out_dir = "concatenated2"
        inp_dir = "input"
    else:
        out_dir = sys.argv[2]
        inp_dir = sys.argv[1]
    for typ in ["train", "valid", "test"]:
        input_dir = f"../resources/{inp_dir}"
        filenames = glob.glob(input_dir + f"/*{typ}*")
        os.makedirs(f"../resources/{out_dir}", exist_ok=True)
        with open(f'../resources/{out_dir}/{typ}_output_file.jsonl', 'w') as outfile:
            for i in range(len(filenames)):
                fname = f"{input_dir}/python_{typ}_{i}.jsonl"
                with open(fname) as infile:
                    for line in infile:
                        a = json.loads(line)
                        outfile.write(json.dumps({"docstring_tokens":a["docstring_tokens"], 'code': a["code"]})+"\n")