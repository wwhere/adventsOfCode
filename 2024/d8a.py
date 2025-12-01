
"""modules"""
from aoc_tools import read_lines

DAY_DATA = "8a"
EMPTY = '.'


class Vector2:
    """A Class with a X and a Y value that can be added and substracted"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, o):
        return Vector2(self.x - o.x, self.y - o.y)

    def __add__(self, o):
        return Vector2(self.x + o.x, self.y + o.y)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __hash__(self):
        return hash((self.x, self.y))


def read_input(filename):
    """Read the daily data

    Args:
        filename (str): Name of the data file

    Returns:
        tuple[list, dict]: the grid and the list of antennas positions
    """
    antennas = {}
    grid = []
    for line in read_lines(filename):
        grid_line = []
        for c in line:
            if c != EMPTY:
                antennas[c] = antennas.get(c, []) + [Vector2(len(grid), len(grid_line))]
            grid_line.append(c)
        grid.append(grid_line)
    return grid, antennas


def in_grid(grid, position: Vector2):
    """Is a position inside a grid

    Args:
        grid (list): A list of lists forming a grid
        position (Vector2): A position (x,y)

    Returns:
        bool: True if the position is inside the grid
    """
    return 0 <= position.x < len(grid) and 0 <= position.y < len(grid[position.x])


def find_antinodes_for_antenna(grid, positions):
    """Finds all antinodes for a list of antenna positions

    Args:
        grid (list): List of lists
        positions (list): List of antenna positions

    Returns:
        list: List of antinode positions
    """
    antinodes = []

    for i1 in range(len(positions)-1):
        for i2 in range(i1+1, len(positions)):
            p1: Vector2 = positions[i1]
            p2: Vector2 = positions[i2]
            dist = p2-p1
            antinode1 = p1 - dist
            antinode2 = p2 + dist
            if in_grid(grid, antinode1):
                antinodes.append(antinode1)
            if in_grid(grid, antinode2):
                antinodes.append(antinode2)

    return antinodes


def process(filename):
    """Process daily

    Args:
        fileName (str): Data file name

    Returns:
        int: solution
    """
    grid, antennas = read_input(filename)

    antinodes = []
    for positions in antennas.values():
        antinodes += find_antinodes_for_antenna(grid, positions)

    antinodes = list(dict.fromkeys(antinodes))

    count = len(antinodes)

    print(f'{filename}: {count}')
    return count


if __name__ == "__main__":
    assert process(f'd{DAY_DATA}.ex.data') == 14
    process(f'd{DAY_DATA}.data')
