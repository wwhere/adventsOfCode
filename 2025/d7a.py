"""Advent of Code specific utilities"""
from aoc_tools import read_lines, remove_duplicates
from collections import defaultdict


def process(filename: str, many_worlds: bool) -> int:
    solution = 0
    t_index = []
    worlds = []
    splits = 0
    for line in read_lines(filename):
        next_t_index = []
        next_worlds = defaultdict(lambda: 0)
        if 'S' in line:
            next_t_index.append(line.index('S'))
            next_worlds[line.index('S')] = 1
        splitters = [i for i, x in enumerate(line) if x == '^']
        for i in t_index:
            if i in splitters:
                splits += 1
                if i > 0:
                    next_t_index.append(i-1)
                    next_worlds[i-1] += worlds[i]
                if i < len(line)-1:
                    next_t_index.append(i+1)
                    next_worlds[i+1] += worlds[i]
            else:
                next_t_index.append(i)
                next_worlds[i] += worlds[i]
        worlds = next_worlds
        t_index = remove_duplicates(next_t_index)

    if not many_worlds:
        solution = splits
    else:
        for t in t_index:
            solution += worlds[t]
    print(f'{filename}: {solution}')
    return solution


def part_1() -> None:
    assert process('d7a.1.data', False) == 21
    process('d7a.2.data', False)


def part_2() -> None:
    assert process('d7a.1.data', True) == 40
    process('d7a.2.data', True)


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
