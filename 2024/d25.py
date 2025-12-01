"""Advent of Code specific utilities"""
from aoc_tools import read_lines

FILL = '#'
EMPTY = '.'


def process(filename: str) -> int:
    solution = 0
    keys = []
    locks = []

    reading = False
    is_key = False
    current = []
    for line in read_lines(filename):
        if not reading:
            is_key = line != '#####'
            current = [0, 0, 0, 0, 0]
            reading = True
        else:
            if len(line) != 5:
                if is_key:
                    for i in range(5):
                        current[i] -= 1
                    keys.append(current)
                else:
                    locks.append(current)
                reading = False
            else:
                for i in range(5):
                    current[i] += 1 if line[i] == FILL else 0

    if is_key:
        for i in range(5):
            current[i] -= 1
        keys.append(current)
    else:
        locks.append(current)

    for key in keys:
        for lock in locks:
            valid = True
            for i in range(5):
                if key[i] + lock[i] > 5:
                    valid = False
                    break
            if valid:
                solution += 1

    print(f'{filename}: {solution}')
    return solution


def part_1() -> None:
    assert process('d25.1.data') == 3
    process('d25.2.data')


def part_2() -> None:
    # assert process('d25.1.data') == 0
    # process('d25.2.data')
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
