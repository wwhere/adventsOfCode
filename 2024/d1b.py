"""modules"""
from collections import defaultdict
from aoc_tools import read_lines


def process(filename):
    """Daily processing

    Args:
        fileName (str): Name of the data file to process

    Returns:
        int: Value for that file
    """
    count = 0
    left = defaultdict(lambda: 0)
    right = defaultdict(lambda: 0)
    for line in read_lines(filename):
        (a, b) = map(int, line.split())
        left[a] += 1
        count += right[a] * a
        right[b] += 1
        count += left[b] * b

    print(f'{filename}: {count}')
    return count


assert process('d1a.ex.data') == 31
process('d1a.data')
