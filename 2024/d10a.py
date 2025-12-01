from aoc_tools import read_lines, remove_duplicates

DAY_DATA = '10a'


def calculate_paths(grid):
    paths = []
    for row in grid:
        paths.append([[] for __ in row])

    for n in range(9, -1, -1):
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 9:
                    increase_adjacents(paths, grid, 8, x, y, [(x, y)])
                elif val == n:
                    increase_adjacents(paths, grid, n-1, x, y, paths[y][x])

    return paths


def increase_adjacents(paths, grid, n, x, y, val):
    if y > 0:
        paths[y-1][x] += val if grid[y-1][x] == n else []
    if x > 0:
        paths[y][x-1] += val if grid[y][x-1] == n else []
    if y < len(paths)-1:
        paths[y+1][x] += val if grid[y+1][x] == n else []
    if x < len(paths[y])-1:
        paths[y][x+1] += val if grid[y][x+1] == n else []


def add_zeroes(paths, zeroes):
    solution = 0

    for zero in zeroes:
        solution += len(remove_duplicates(paths[zero[0]][zero[1]]))

    return solution


def process(filename: str) -> int:
    solution = 0
    grid = []
    zeroes = []
    for line in read_lines(filename):
        row = []
        for x, c in enumerate(line):
            y = len(grid)
            if c == '0':
                zeroes.append((y, x))
            row.append(int(c))
        grid.append(row)

    paths = calculate_paths(grid)
    solution = add_zeroes(paths, zeroes)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process(f'd{DAY_DATA}.ex.data') == 1
    assert process(f'd{DAY_DATA}.ex2.data') == 36
    process(f'd{DAY_DATA}.data')
