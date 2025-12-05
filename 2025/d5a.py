"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename: str, part_2: bool) -> int:
    solution = 0
    reading_ranges = True
    ranges = []
    for line in read_lines(filename):
        if len(line) < 1:
            reading_ranges = False
            if part_2:
                break
            continue

        if reading_ranges:
            [minimum, maximum] = [int(x) for x in line.split('-')]
            if part_2:
                new_ranges = []
                for (a, b) in ranges:
                    if minimum > b+1 or maximum < a-1:
                        new_ranges.append([a, b])
                    elif minimum == b + 1:
                        minimum = a
                    elif maximum == a - 1:
                        maximum = b
                    elif minimum <= a and maximum >= a:
                        maximum = max(b, maximum)
                    elif minimum >= a and maximum <= b:
                        minimum = a
                        maximum = b
                    elif minimum <= b and maximum >= b:
                        minimum = min(a, minimum)
                    elif minimum < a and maximum > b:
                        continue
                new_ranges.append([minimum, maximum])
                ranges = new_ranges
                pass
            else:
                ranges.append([minimum, maximum])
        else:
            solution += 1 if is_fresh(int(line), ranges) else 0

    if part_2:
        ranges.sort(key=sort_func)
        for [minimum, maximum] in ranges:
            solution += maximum-minimum+1

    print(f'{filename}: {solution}')
    return solution


def sort_func(x):
    return x[0]


def is_fresh(id: int, ranges) -> bool:
    for (min, max) in ranges:
        if id >= min and id <= max:
            return True
    return False


def part_1() -> None:
    assert process('d5a.1.data', False) == 3
    process('d5a.2.data', False)


def part_2() -> None:
    assert process('d5a.1.data', True) == 14
    process('d5a.2.data', True)
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
