"""Advent of Code specific utilities"""
from aoc_tools import read_lines
from d15a import get_next_position, in_grid

BOX = 'O'
WALL = '#'
ROBOT = '@'
EMPTY = '.'
UP = '^'
RIGHT = '>'
DOWN = 'v'
LEFT = '<'
BOX_LEFT = '['
BOX_RIGHT = ']'


def try_move_horizontally(grid, position, direction):
    if grid[position[0]][position[1]] == EMPTY:
        return True, position

    if grid[position[0]][position[1]] == WALL:
        return False, position

    next_position = get_next_position(position, direction)

    if not in_grid(grid, next_position):
        return False, position

    can_move, __ = try_move_horizontally(grid, next_position, direction)
    if can_move:
        grid[next_position[0]][next_position[1]] = grid[position[0]][position[1]]
        grid[position[0]][position[1]] = EMPTY
        return True, next_position

    return False, position


def try_move_vertically(grid, position, direction, do_move=False):
    if grid[position[0]][position[1]] == EMPTY:
        return True, position

    if grid[position[0]][position[1]] == WALL:
        return False, position

    if grid[position[0]][position[1]] == ROBOT:
        next_position = get_next_position(position, direction)

        if not in_grid(grid, next_position):
            return False, position

        can_move, __ = try_move_vertically(grid, next_position, direction)
        if can_move:
            try_move_vertically(grid, next_position, direction, True)
            grid[next_position[0]][next_position[1]] = grid[position[0]][position[1]]
            grid[position[0]][position[1]] = EMPTY
            return True, next_position

        return False, position

    if grid[position[0]][position[1]] == BOX_LEFT:
        next_position_l = get_next_position(position, direction)
        next_position_r = get_next_position((position[0], position[1]+1), direction)

        if not in_grid(grid, next_position_l) or not in_grid(grid, next_position_r):
            return False, position

        can_move_l, __ = try_move_vertically(grid, next_position_l, direction, do_move)
        can_move_r, __ = try_move_vertically(grid, next_position_r, direction, do_move)

        if can_move_l and can_move_r:
            if do_move:
                grid[next_position_l[0]][next_position_l[1]] = grid[position[0]][position[1]]
                grid[next_position_r[0]][next_position_r[1]] = grid[position[0]][position[1]+1]
                grid[position[0]][position[1]] = EMPTY
                grid[position[0]][position[1]+1] = EMPTY
            return True, next_position_l

        return False, position

    if grid[position[0]][position[1]] == BOX_RIGHT:
        next_position_r = get_next_position(position, direction)
        next_position_l = get_next_position((position[0], position[1]-1), direction)

        if not in_grid(grid, next_position_l) or not in_grid(grid, next_position_r):
            return False, position

        can_move_l, __ = try_move_vertically(grid, next_position_l, direction, do_move)
        can_move_r, __ = try_move_vertically(grid, next_position_r, direction, do_move)

        if can_move_l and can_move_r:
            if do_move:
                grid[next_position_r[0]][next_position_r[1]] = grid[position[0]][position[1]]
                grid[next_position_l[0]][next_position_l[1]] = grid[position[0]][position[1]-1]
                grid[position[0]][position[1]] = EMPTY
                grid[position[0]][position[1]-1] = EMPTY
            return True, next_position_r

        return False, position


def get_final_grid(grid, robot_position, moves, do_print=False):
    if do_print:
        print('Initial grid:')
        print_grid(grid)

    for move in moves:
        if move in [LEFT, RIGHT]:
            __, robot_position = try_move_horizontally(grid, robot_position, move)
        else:
            __, robot_position = try_move_vertically(grid, robot_position, move)
        if do_print:
            print('')
            print(f'Move {move}:')
            print_grid(grid)
    return grid


def get_gps(grid):
    total = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == BOX_LEFT:
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
                    row.append(ROBOT)
                    row.append(EMPTY)
                elif c == WALL:
                    row.append(WALL)
                    row.append(WALL)
                elif c == BOX:
                    row.append(BOX_LEFT)
                    row.append(BOX_RIGHT)
                elif c == EMPTY:
                    row.append(EMPTY)
                    row.append(EMPTY)
            grid.append(row)

    final_grid = get_final_grid(grid, robot_position, moves, False)

    solution = get_gps(final_grid)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d15.2.data') == 9021
    process('d15.3.data')
