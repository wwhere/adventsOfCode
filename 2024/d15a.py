"""Advent of Code specific utilities"""
from aoc_tools import read_lines

BOX = 'O'
WALL = '#'
ROBOT = '@'
EMPTY = '.'
UP = '^'
RIGHT = '>'
DOWN = 'v'
LEFT = '<'


def get_next_position(position, direction):
    if direction == UP:
        return (position[0]-1, position[1])
    if direction == RIGHT:
        return (position[0], position[1]+1)
    if direction == DOWN:
        return (position[0]+1, position[1])
    if direction == LEFT:
        return (position[0], position[1]-1)


def in_grid(grid, position):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[position[0]])


def try_move(grid, position, direction):
    if grid[position[0]][position[1]] == EMPTY:
        return True, position

    if grid[position[0]][position[1]] == WALL:
        return False, position

    next_position = get_next_position(position, direction)

    if not in_grid(grid, next_position):
        return False, position

    can_move, __ = try_move(grid, next_position, direction)
    if can_move:
        grid[next_position[0]][next_position[1]] = grid[position[0]][position[1]]
        grid[position[0]][position[1]] = EMPTY
        return True, next_position

    return False, position


def get_final_grid(grid, robot_position, moves):
    for move in moves:
        __, robot_position = try_move(grid, robot_position, move)

    return grid


def get_gps(grid):
    total = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == BOX:
                total += 100*y + x

    return total


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def process(filename: str) -> int:
    solution = 0
    reading_moves = False
    grid = []
    moves = []
    robot_position = (0, 0)
    for line in read_lines(filename):
        if line == '':
            reading_moves = True
            continue

        if reading_moves:
            for m in line:
                moves.append(m)
        else:
            row = []
            for c in line:
                if c == ROBOT:
                    robot_position = (len(grid), len(row))
                row.append(c)
            grid.append(row)

    final_grid = get_final_grid(grid, robot_position, moves)

    solution = get_gps(final_grid)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d15.1.data') == 2028
    assert process('d15.2.data') == 10092
    process('d15.3.data')
