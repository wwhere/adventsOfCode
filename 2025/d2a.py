"""Advent of Code specific utilities"""
from aoc_tools import read_lines
import math


def process(filename: str, justInTwo: bool) -> int:
    solution = 0
    for line in read_lines(filename):
        segments = line.split(',')
        for segment in segments:
            correct = []
            [a, b] = segment.split('-')
            na = int(a)
            nb = int(b)
            la = len(a)
            lb = len(b)
            hla = int(a[0:la // 2]) if la > 1 else 0
            hlb = int(b[0:lb // 2]) if lb > 1 else 0
            for r in range(hla, max(hlb+1, hla*10)):
                # print(f'Checking half {r} between {a}-{b} ({hla}-{hlb})')
                for x in range(1, len(f'{r}')+1):
                    part_x = f'{r}'[0:x]
                    for repetitions in range(2, 11):
                        if justInTwo and repetitions != 2:
                            continue
                        y = int(part_x * repetitions)
                        if y >= na and y <= nb:
                            correct.append(y)
            correct_set = set(correct)
            # print(f'correct solutions: {correct_set}')
            for c in correct_set:
                solution += c
            correct = []
        continue

    print(f'{filename}: {solution}')
    return solution


def part_1() -> None:
    assert process('d2a.1.data', True) == 1227775554
    process('d2a.2.data', True)


def part_2() -> None:
    assert process('d2a.1.data', False) == 4174379265
    process('d2a.2.data', False)
    pass


def main() -> None:
    # part_1()
    part_2()


if __name__ == "__main__":
    main()
