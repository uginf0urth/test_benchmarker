import args
import cmd
import os
import glob
import tools


def clean():
    for f in glob.glob("massif.out.*"):
        os.remove(f)


def evaluate_assigner_performance(path):
    a_massif_out_index = cmd.create_valgrind_report_for_assigner(path)
    if a_massif_out_index == "":
        print("failed to get assigner massif.out index")
        exit(0)
    else:
        print("valgrind assigner succeed")
    assigner_amount_memory_in_bytes = tools.get_amount_memory_used_from_massif(a_massif_out_index)
    assigner_amount_memory_in_gb = assigner_amount_memory_in_bytes / (1024 ** 3)

    assigner_time = cmd.create_time_report_for_assigner(path)

    return assigner_amount_memory_in_gb, assigner_time


def evalute_proof_generator_performance(path):
    pg_massif_out_index = cmd.create_valgrind_report_for_proof_generator(path)
    if pg_massif_out_index == "":
        print("failed to get pg massif.out index")
        exit(0)
    else:
        print("valgrind proof generator succeed")
    pg_amount_memory_in_bytes = tools.get_amount_memory_used_from_massif(pg_massif_out_index)
    pg_amount_memory_in_gb = pg_amount_memory_in_bytes / (1024 ** 3)

    pg_time = cmd.create_time_report_for_proof_generator(path)

    return pg_amount_memory_in_gb, pg_time


def main():
    repo_path = args.get_zkllvm_path()

    if not os.path.isfile("{}scripts/run.sh".format(repo_path)):
        print("file scripts/run.sh does not exist in repo path")
        exit(0)

    cmd.compile_zkllvm(repo_path)

    a_memory, a_time = evaluate_assigner_performance(repo_path)
    pg_memory, pg_time = evalute_proof_generator_performance(repo_path)

    print("1. Assigner\n    1. memory: {}Gb\n    2. time: {}".format(round(a_memory, 3), a_time))
    print("2. Proof generator\n    1. memory: {}Gb\n    2. time: {}".format(round(pg_memory, 3), pg_time))


if __name__ == '__main__':
    main()
    clean()
