"""Advent of Code specific utilities"""
from aoc_tools import read_lines

TRACK = '.'
START = 'S'
END = 'E'
WALL = '#'


def get_next_step(grid, pos, visited):
    y, x = pos

    if y+1 < len(grid) and grid[y+1][x] in [TRACK, END] and (y+1, x) not in visited:
        return (y+1, x)
    if 0 <= y-1 and grid[y-1][x] in [TRACK, END] and (y-1, x) not in visited:
        return (y-1, x)
    if x+1 < len(grid[y]) and grid[y][x+1] in [TRACK, END] and (y, x+1) not in visited:
        return (y, x+1)
    if 0 <= x-1 and grid[y][x-1] in [TRACK, END] and (y, x-1) not in visited:
        return (y, x-1)


def number_grid(grid, start_position):
    steps = []

    pos = start_position
    count = 0

    while grid[pos[0]][pos[1]] != END:
        steps.append((pos[0], pos[1]))
        count += 1
        pos = get_next_step(grid, pos, steps)

    steps.append((pos[0], pos[1]))

    return steps


def get_cheats(steps, min_save):
    cheats = 0
    number_of_steps = len(steps)
    for count in range(number_of_steps-min_save):
        y, x = steps[count]
        for c in range(count+min_save, number_of_steps):
            exit_y, exit_x = steps[c]
            distance = abs(exit_x-x)+abs(exit_y-y)
            cheat_save = c - (count+distance)
            if distance <= 20 and cheat_save >= min_save:
                cheats += 1
    return cheats


def process(filename: str, min_save: int) -> int:
    solution = 0
    grid = []
    start_position = (0, 0)
    for line in read_lines(filename):
        row = list(line)
        if START in line:
            start_position = (len(grid), line.index(START))
        grid.append(row)

    steps = number_grid(grid, start_position)

    solution = get_cheats(steps, min_save)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    process('d20.1.data', 50)
    process('d20.2.data', 100)
