import glob
import os

if __name__ == '__main__':
    for typ in ["train", "valid", "test"]:
        input_dir = "./extract_res"
        filenames = glob.glob(input_dir+f"/*{typ}*")
        os.makedirs("./concatenated", exist_ok=True)
        with open(f'./concatenated/{typ}_output_file.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)