"""Advent of Code specific utilities"""
from functools import reduce
from operator import mul
from aoc_tools import read_lines


def display(robots, width, height, seconds):

    grid = [[0 for __ in range(width)] for __ in range(height)]
    for robot in robots:
        x = (robot[0][0] + robot[1][0] * seconds) % width
        y = (robot[0][1] + robot[1][1] * seconds) % height
        grid[y][x] += 1

    disp = False

    for h in range(height):
        line = ''
        for w in range(width):
            line += str(grid[h][w]) if grid[h][w] != 0 else ' '
            if '1111111111111111111111111111111' in line:
                disp = True

    return disp


def solve_all(robots, width, height):
    for s in range(30000):
        if display(robots, width, height, s):
            print(f'({s} seconds)')


def process(filename: str, width, height) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    robots = []
    for line in read_lines(filename):
        p, v = line.replace('p=', '').split(' v=')
        p_x, p_y = p.split(',')
        v_x, v_y = v.split(',')
        robots.append(((int(p_x), int(p_y)), (int(v_x), int(v_y))))

    solve_all(robots, width, height)


if __name__ == "__main__":
    # process('d14.1.data', 11, 7, 100)
    process('d14.2.data', 101, 103)
