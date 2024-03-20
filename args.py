import os
import argparse


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--zkllvm-path", required=True, type=dir_path)
    return parser.parse_args()


def get_zkllvm_path() -> str:
    args = get_args()

    return args.zkllvm_path
