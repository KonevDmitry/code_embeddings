#!/usr/bin/env bash

python ./python_ast.py
python ./extract.py
python ./concater.py
/bin/bash ./preprocess.sh