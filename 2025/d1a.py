"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename: str, every_click: bool) -> int:
    solution = 0
    previous = 50    
    dial_size = 100
    for line in read_lines(filename):
        modifier = int(line[1:]) * (-1 if line[0:1] == "L" else 1)
        current = previous + modifier
        if not every_click:
            if current % dial_size == 0:
                solution += 1
        else:
            solution += abs(current) // dial_size
            if modifier < 0 and abs(modifier) >= previous and previous > 0:
                solution += 1
            current = current % dial_size
        previous = current
        continue

    print(f'{filename} counting all clicks {every_click}: {solution}')
    return solution


def part_1() -> None:
    assert process('d1a.1.data', False) == 3
    process('d1a.2.data', False)


def part_2() -> None:
    assert process('d1a.1.data', True) == 6
    process('d1a.2.data', True)


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
