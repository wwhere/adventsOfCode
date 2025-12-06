"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename: str) -> int:
    solution = 0
    numbers = []
    operations = []
    for line in read_lines(filename):
        if '+' in line:
            operations = list(line)
        else:
            numbers.append(list(line))

    current_op = ''
    first_index = 0
    last_index = 0
    for index, op in enumerate(operations):
        if op == '+' or op == '*':
            if current_op == '':
                current_op = op
                first_index = index
            else:
                last_index = index-2
                solution += calculate(current_op, first_index, last_index, numbers)
                current_op = op
                first_index = index
    last_index = len(operations)-1
    solution += calculate(current_op, first_index, last_index, numbers)
    print(f'{filename}: {solution}')
    return solution


def calculate(op: str, a: int, b: int, numbers) -> int:
    total = 1 if op == '*' else 0
    for i in range(b, a-1, -1):
        number = ''
        for n in numbers:
            if n[i] != '':
                number = f'{number}{n[i]}'
        number_int = int(number)
        if (op == '*'):
            total *= number_int
        elif (op == '+'):
            total += number_int
    return total


def part_1() -> None:
    # assert process('d6a.1.data') == 4277556
    # process('d6a.2.data')
    pass


def part_2() -> None:
    assert process('d6a.1.data') == 3263827
    process('d6a.2.data')
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
