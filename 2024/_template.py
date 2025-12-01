"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename: str) -> int:
    solution = 0
    for line in read_lines(filename):
        continue

    print(f'{filename}: {solution}')
    return solution


def part_1() -> None:
    assert process('dXX.1.data') == 0
    process('dXX.2.data')


def part_2() -> None:
    # assert process('dXX.1.data') == 0
    # process('dXX.2.data')
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
