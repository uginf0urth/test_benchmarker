import msparser
import os


def get_amount_memory_used_from_massif(index):
    data = msparser.parse_file('{}/massif.out.{}'.format(os.getcwd(), index))

    a = []
    for snapshot in data['snapshots']:
        total = snapshot['mem_heap'] + snapshot['mem_heap_extra']
        a.append(total)

    return max(a)
