"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename: str, amount: int) -> int:
    solution = 0
    for bank in read_lines(filename):
        joltage = [0] * amount
        for index, battery in enumerate(bank):
            value = int(battery)
            for digit in range(amount-1, -1, -1):
                if value > joltage[digit] and index < len(bank)-digit:
                    joltage[digit] = value
                    for d in range(0, digit):
                        joltage[d] = 0
                    break

        for index, jolt in enumerate(joltage):
            solution += jolt * pow(10, index)
        continue

    print(f'{filename}: {solution}')
    return solution


def part_1() -> None:
    assert process('d3a.1.data', 2) == 357
    process('d3a.2.data', 2)


def part_2() -> None:
    assert process('d3a.1.data', 12) == 3121910778619
    process('d3a.2.data', 12)
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
