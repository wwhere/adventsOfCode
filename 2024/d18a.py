"""Advent of Code specific utilities"""
from aoc_tools import read_lines

EMPTY = '.'
WALL = '#'


class Step:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __str__(self):
        return f'{self.x}/{self.y}({self.cost})'

    def __repr__(self):
        return self.__str__()


def get_next_steps(grid, step: Step):
    options = [
        Step(step.x+1, step.y, step.cost+1),
        Step(step.x-1, step.y, step.cost+1),
        Step(step.x, step.y+1, step.cost+1),
        Step(step.x, step.y-1, step.cost+1),
    ]
    next_steps = []
    for next_step in options:
        if 0 <= next_step.y < len(grid) and 0 <= next_step.x < len(grid[next_step.y]):
            if grid[next_step.y][next_step.x] != WALL:
                next_steps.append(next_step)
    return next_steps


def find_min_path(grid, start, end):
    next_steps: list[Step] = []
    size = len(grid)
    costs = [[size*size for __ in range(size)] for __ in range(size)]
    next_steps.append(Step(start[0], start[1], 0))

    while len(next_steps) > 0:
        step = next_steps.pop()
        if costs[step.y][step.x] > step.cost:
            costs[step.y][step.x] = step.cost
            next_steps += get_next_steps(grid, step)

    return costs[end[0]][end[1]]


def process(filename: str, size: int, max_bytes: int = 10000) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    solution = 0

    grid = [[EMPTY for __ in range(size)] for __ in range(size)]

    byte = 0
    for line in read_lines(filename):
        if byte < max_bytes:
            x, y = (map(int, line.split(',')))
            grid[y][x] = WALL
            byte += 1
            continue
        break

    solution = find_min_path(grid, (0, 0), (size-1, size-1))

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d18.1.data', 7, 12) == 22
    process('d18.2.data', 71, 1024)
