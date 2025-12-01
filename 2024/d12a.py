"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def marching(grid, row, column):
    area = 0
    perimeter = 0
    region = grid[row][column]

    to_check = [(row, column)]
    in_area = []

    while len(to_check) > 0:
        r, c = to_check.pop()
        if (r, c) in in_area:
            continue
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != region:
            perimeter += 1
            continue
        area += 1
        to_check.append((r+1, c))
        to_check.append((r-1, c))
        to_check.append((r, c+1))
        to_check.append((r, c-1))
        grid[r][c] = ''
        in_area.append((r, c))

    # print(f'Region {region} has area {area} and perimeter {perimeter}')

    return area * perimeter


def solve(grid):
    total = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == '':
                continue
            total += marching(grid, row, column)

    return total


def process(filename: str) -> int:
    solution = 0
    grid = []
    for line in read_lines(filename):
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    solution = solve(grid)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d12a.ex2.data') == 140
    assert process('d12a.ex3.data') == 772
    assert process('d12a.ex.data') == 1930
    process('d12a.data')
