"""Advent of Code specific utilities"""
from aoc_tools import read_lines
from typing import NamedTuple


class Tile(NamedTuple):
    x: int
    y: int


def process(filename: str) -> int:
    solution = 0
    tiles: list[NamedTuple] = []
    for line in read_lines(filename):
        [x, y] = line.split(',')
        new_tile = Tile(int(x), int(y))
        for tile in tiles:
            area = (abs(tile.x-new_tile.x)+1) * (abs(tile.y-new_tile.y)+1)
            if area > solution:
                solution = area
        tiles.append(new_tile)

    print(f'{filename}: {solution}')
    return solution


def part_1() -> None:
    assert process('d9a.1.data') == 50
    process('d9a.2.data')


def part_2() -> None:
    # assert process('d9a.1.data') == 0
    # process('d9a.2.data')
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
