"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename: str) -> int:
    solution = 0
    numbers = []
    operations = []
    for line in read_lines(filename):
        if '+' in line:
            operations = line.split()
        else:
            numbers.append(line.split())

    for index, op in enumerate(operations):
        if op == '+':
            s = 0
            for n in numbers:
                s += int(n[index])
            solution += s
        else:
            s = 1
            for n in numbers:
                s *= int(n[index])
            solution += s

    print(f'{filename}: {solution}')
    return solution


def part_1() -> None:
    assert process('d6a.1.data') == 4277556
    process('d6a.2.data')


def part_2() -> None:
    # assert process('d6a.1.data') == 0
    # process('d6a.2.data')
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
