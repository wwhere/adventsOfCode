"""Advent of Code specific utilities"""
from aoc_tools import read_lines
from collections import defaultdict

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

    raise Exception(f'No more path after {pos}')


def number_grid(grid, start_position):
    steps = [[-1 for __ in grid[0]] for __ in grid]

    pos = start_position
    count = 0
    visited = []

    while grid[pos[0]][pos[1]] != END:
        steps[pos[0]][pos[1]] = count
        count += 1
        visited.append(pos)
        pos = get_next_step(grid, pos, visited)

    steps[pos[0]][pos[1]] = count

    return steps, count


def get_cheats(grid, start_position, steps):
    cheats = defaultdict(lambda: [])

    pos = start_position
    count = 0
    visited = []

    while grid[pos[0]][pos[1]] != END:

        cheat_up = (pos[0]-2, pos[1])
        cheat_down = (pos[0]+2, pos[1])
        cheat_right = (pos[0], pos[1]+2)
        cheat_left = (pos[0], pos[1]-2)
        for c in [cheat_down, cheat_left, cheat_right, cheat_up]:
            y, x = c
            if 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] in [TRACK, END]:
                cheat_save = steps[y][x] - (count+2)
                if cheat_save > 0:
                    cheats[cheat_save] = cheats[cheat_save] + [(pos[0], pos[1], y, x)]

        count += 1
        visited.append(pos)
        pos = get_next_step(grid, pos, visited)

    return cheats


def process(filename: str) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    solution = 0
    grid = []
    start_position = (0, 0)
    for line in read_lines(filename):
        row = list(line)
        if START in line:
            start_position = (len(grid), line.index(START))
        grid.append(row)

    steps, max_picoseconds = number_grid(grid, start_position)

    cheats = get_cheats(grid, start_position, steps)

    times = sorted(cheats.keys())
    solution = 0
    for time in times:
        if time >= 100:
            solution += len(cheats[time])
        print(f'{len(cheats[time])} cheats save {time} picoseconds')

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d20.1.data') == 0
    process('d20.2.data')
