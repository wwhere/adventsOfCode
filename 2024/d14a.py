"""Advent of Code specific utilities"""
from functools import reduce
from operator import mul
from aoc_tools import read_lines


def solve(robot, width, height, seconds):

    x = (robot[0][0] + robot[1][0] * seconds) % width
    y = (robot[0][1] + robot[1][1] * seconds) % height

    if x < width // 2:
        if y < height // 2:
            return 0
        elif y > height // 2:
            return 2
    elif x > width // 2:
        if y < height // 2:
            return 1
        elif y > height // 2:
            return 3

    return -1


def solve_all(robots, width, height, seconds):
    total = [0, 0, 0, 0]

    for robot in robots:
        q = solve(robot, width, height, seconds)
        if q >= 0:
            total[q] += 1

    return reduce(mul, total)


def process(filename: str, width, height, seconds) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    solution = 0
    robots = []
    for line in read_lines(filename):
        p, v = line.replace('p=', '').split(' v=')
        p_x, p_y = p.split(',')
        v_x, v_y = v.split(',')
        robots.append(((int(p_x), int(p_y)), (int(v_x), int(v_y))))

    solution = solve_all(robots, width, height, seconds)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d14.1.data', 11, 7, 100) == 12
    process('d14.2.data', 101, 103, 100)
