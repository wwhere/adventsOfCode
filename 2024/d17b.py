"""Advent of Code specific utilities"""
from aoc_tools import read_lines
from d17a import Device


def process(filename: str) -> int:
    device = Device()
    expected = []

    for line in read_lines(filename):
        if 'Program:' in line:
            expected = line.replace('Program: ', '').split(',')
            device.program = [int(i) for i in line.replace('Program: ', '').split(',')]
            continue

    solution: int = 0
    for i in range(1, len(expected)+1):
        current_expected = ','.join(expected[len(expected)-i:])
        for a in range(0, 64):
            base = (solution << 3) + a
            device.a = base
            device.b = 0
            device.c = 0
            run_output = device.execute()
            if current_expected == run_output:
                print(base, '=', run_output, '/', bin(base))
                solution = base
                break

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d17.3.data') == 117440
    process('d17.2.data')
