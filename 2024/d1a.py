"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename):
    """Main processing for the day"""
    count = 0
    list_a = []
    list_b = []

    for line in read_lines(filename):
        a, b = map(int, line.split())
        list_a.append(a)
        list_b.append(b)

    list_a.sort()
    list_b.sort()

    for a, b in zip(list_a, list_b):
        count += abs(a-b)

    print(f'{filename}: {count}')
    return count


assert process('d1a.ex.data') == 11
process('d1a.data')
