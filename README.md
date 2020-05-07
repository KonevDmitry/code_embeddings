# code_embeddings

To run our program you have to:
1) Run requierements.txt
2) Put input data inside the folder resources/input
3) Run runner.sh
4) Run the train.sh that is inside the model114 folder
5) Wait for as long as you want
6) Modify test.sh to use the latest model version (change 27 in ```--load ${model_dir}/model_iter27``` to the latest epoch saved, which can be seen in the folder model114/models/python/)
7) Run test.sh
8) From the folder model114/models/python/ copy file pred.txt into the folder resources/input
9) Run from the folder fulltext file inserter_ast.py
10) Run the flask app (which is app.py)

The dataset that we used is [CodeSearchNet](https://github.com/github/CodeSearchNet).

If you don't want to train the model yourself, you can [take the one we trained](https://drive.google.com/file/d/15s7_QcD8FB2bhjuf0KX7ptpk5iLeMKDI/view?usp=sharing) for 28 epoch. You can use it for further training or take its pred.txt (which lies in the same folder).
