"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename: str, it: bool) -> int:
    solution = 0
    grid = []
    for line in read_lines(filename):
        grid.append(list(line))
        continue

    (amount, new_grid) = process_grid(grid)
    solution += amount

    while (amount > 0 and it):
        (amount, new_grid) = process_grid(new_grid)
        solution += amount

    print(f'{filename}: {solution}')
    return solution


def process_grid(grid):
    solution = 0
    removed_rolls = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '.':
                continue
            rolls = 0
            for a in range(y-1, y+2):
                if a < 0 or a >= len(grid):
                    continue
                for b in range(x-1, x+2):
                    if a == y and b == x:
                        continue
                    if b < 0 or b >= len(grid[0]):
                        continue
                    if grid[a][b] == '@':
                        rolls += 1
            if rolls < 4:
                solution += 1
                removed_rolls.append([y, x])
    for [y, x] in removed_rolls:
        grid[y][x] = '.'
    return (solution, grid)


def part_1() -> None:
    assert process('d4a.1.data', False) == 13
    process('d4a.2.data', False)


def part_2() -> None:
    assert process('d4a.1.data', True) == 43
    process('d4a.2.data', True)
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
