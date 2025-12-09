"""Advent of Code specific utilities"""
from aoc_tools import read_lines
from typing import NamedTuple
from shapely.geometry.polygon import Polygon


def get_area(a, b) -> int:
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)


def process(filename: str) -> int:
    solution = 0
    tiles = []
    for line in read_lines(filename):
        [x, y] = line.split(',')
        tiles.append([int(x), int(y)])
    complete_polygon = Polygon(tiles)

    for a in tiles:
        for b in tiles:
            if a == b:
                continue
            area = get_area(a, b)
            if area > solution:
                polygon = Polygon([a, [a[0], b[1]], b, [b[0], a[1]]])
                if complete_polygon.contains(polygon):
                    solution = area

    print(f'{filename}: {solution}')
    return solution


def part_1() -> None:
    # assert process('d9a.1.data') == 50
    # process('d9a.2.data')
    pass


def part_2() -> None:
    assert process('d9a.1.data') == 24
    assert process('d9a.2.data')


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
