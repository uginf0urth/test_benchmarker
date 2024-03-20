# Readme
This is the simple test script for benchmarking zkllvm assigner and proof generator.

Make sure that all dependencies from the repositories listed below have been installed.

- [zkLLVM](https://github.com/NilFoundation/zkLLVM)

- [proof-producer](https://github.com/NilFoundation/proof-producer)

- [zkllvm-template](https://github.com/NilFoundation/zkllvm-template)

In addition, make sure you have the utilities **valgrind** and **massif-visualizer**.

---

Before run the script don't forget install requirements:

 	`pip install -r requirements.txt`


### Example:

Use `--zkllvm-path` param for determine directory with repository.

    python3 main.py --zkllvm-path=/home/{user}/zkllvm-template/

