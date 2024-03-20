import os
import subprocess
import re
from pytimeparse.timeparse import timeparse

regExpIndex = re.compile('^\D*(\d*)\D*$')
regExpTime = re.compile('(\d*):(\d{2}).(\d{2})elapsed')


def subprocess_init(cmd):
    s = subprocess.getstatusoutput(cmd)

    if s[0] != 0:
        raise Exception('Custom Error {}'.format(s[1]))

    return s[1]


def compile_zkllvm(path):
    print("compile zkllvm-template")
    try:
        _ = subprocess_init("sudo bash {}scripts/run.sh compile".format(path))
    except Exception as err:
        print(err)
        exit(0)
    else:
        print("compile successfully")


def create_valgrind_report_for_assigner(path):
    print("start valgrind assigner")
    try:
        out = subprocess_init("valgrind \
        --tool=massif \
        assigner \
        -b {0}build/src/template.ll \
        -p {0}./src/main-input.json \
        -c {0}build/src/template.crct \
        -t {0}build/src/template.tbl \
        -e pallas".format(path))
    except Exception as err:
        print(err)
        exit(0)
    else:
        # regular functions like replace and translate are not so good
        # because the source contains additional characters
        string_arr = out.splitlines()
        return regExpIndex.search(string_arr[-1]).group(1)


def create_time_report_for_assigner(path):
    print("start time assigner")
    try:
        out = subprocess_init("time \
        assigner \
        -b {0}build/src/template.ll \
        -p {0}./src/main-input.json \
        -c {0}build/src/template.crct \
        -t {0}build/src/template.tbl \
        -e pallas".format(path))
    except Exception as err:
        print(err)
        exit(0)
    else:
        minutes = regExpTime.search(out).group(1)
        seconds = regExpTime.search(out).group(2)
        milliseconds = regExpTime.search(out).group(3)

        return str("{}m{}s{}0ms".format(minutes, seconds, milliseconds))


def create_valgrind_report_for_proof_generator(path):
    print("start valgrind proof generator")
    try:
        out = subprocess_init("valgrind \
        --tool=massif \
        proof-generator-single-threaded \
        ---circuit  {0}build/src/template.crct \
        --assignment {0}build/src/template.tbl \
        --proof {0}build/proof.bin".format(path))
    except Exception as err:
        print(err)
        exit(0)
    else:
        # regular functions like replace and translate are not so good
        # because the source contains additional characters
        string_arr = out.splitlines()
        return regExpIndex.search(string_arr[-1]).group(1)


def create_time_report_for_proof_generator(path):
    print("start time assigner")
    try:
        out = subprocess_init("time \
        proof-generator-single-threaded \
        --circuit  {0}build/src/template.crct \
        --assignment {0}build/src/template.tbl \
        --proof {0}build/proof.bin".format(path))
    except Exception as err:
        print(err)
        exit(0)
    else:
        minutes = regExpTime.search(out).group(1)
        seconds = regExpTime.search(out).group(2)
        milliseconds = regExpTime.search(out).group(3)

        return str("{}m{}s{}0ms".format(minutes, seconds, milliseconds))
