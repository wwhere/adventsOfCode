"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def calculate_sides(perimeter):
    total = 0
    original_perimeter = []
    for p in perimeter:
        original_perimeter.append((p[0], p[1], p[2]))
    while len(perimeter) > 0:
        total += 1
        kind, r, c = perimeter.pop()
        if kind == 'R':
            found = True
            col = c+1
            while found:
                if (kind, r, col) in perimeter and ('C', r-1, col) not in original_perimeter and ('C', r, col) not in original_perimeter:
                    perimeter.remove((kind, r, col))
                    col += 1
                else:
                    found = False
            found = True
            col = c-1
            while found:
                if (kind, r, col) in perimeter and ('C', r-1, col+1) not in original_perimeter and ('C', r, col+1) not in original_perimeter:
                    perimeter.remove((kind, r, col))
                    col -= 1
                else:
                    found = False
        else:
            found = True
            row = r+1
            while found:
                if (kind, row, c) in perimeter and ('R', row, c-1) not in original_perimeter and ('R', row, c) not in original_perimeter:
                    perimeter.remove((kind, row, c))
                    row += 1
                else:
                    found = False
            found = True
            row = r-1
            while found:
                if (kind, row, c) in perimeter and ('R', row+1, c-1) not in original_perimeter and ('R', row+1, c) not in original_perimeter:
                    perimeter.remove((kind, row, c))
                    row -= 1
                else:
                    found = False
    return total


def marching(grid, row, column):
    area = 0
    perimeter = 0
    region = grid[row][column]

    to_check = [(row, column, ('', 0, 0))]
    in_area = []
    perimeter = []

    while len(to_check) > 0:
        r, c, p = to_check.pop()
        if (r, c) in in_area:
            continue
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != region:
            perimeter.append(p)
            continue
        area += 1
        to_check.append((r+1, c, ('R', r+1, c)))
        to_check.append((r-1, c, ('R', r, c)))
        to_check.append((r, c+1, ('C', r, c+1)))
        to_check.append((r, c-1, ('C', r, c)))
        grid[r][c] = ''
        in_area.append((r, c))

    sides = calculate_sides(perimeter)

    return area * sides


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
    assert process('d12b.ex2.data') == 368
    assert process('d12b.ex4.data') == 68
    assert process('d12a.ex2.data') == 80
    assert process('d12a.ex3.data') == 436
    assert process('d12b.ex.data') == 236
    assert process('d12a.ex.data') == 1206
    process('d12a.data')
