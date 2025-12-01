"""Advent of Code specific utilities"""
from collections import defaultdict
from aoc_tools import read_lines


def get_graph(towels):
    start_node = defaultdict(lambda: [])

    for towel in towels:
        first = towel[:1]
        start_node[first] = start_node[first] + [towel]

    return start_node


def possible_ways(design, graph, cache: dict):
    if design in cache.keys():
        return cache[design]
    first = design[:1]

    ways = 1 if len(design) == 0 else 0

    for towel in graph[first]:
        if design.startswith(towel):
            ways += possible_ways(design[len(towel):], graph, cache)

    cache[design] = ways
    return ways


def solve(towels: list[str], designs: list[str]):
    total = 0
    cache = {}

    graph = get_graph(towels)
    for design in designs:
        ways = possible_ways(design, graph, cache)
        total += ways

    return total


def process(filename: str) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    solution = 0
    towels = []
    designs = []
    towels_read = False
    for line in read_lines(filename):
        if not towels_read:
            towels = line.split(', ')
            towels_read = True
            continue

        if len(line) > 1:
            designs.append(line)

    solution = solve(towels, designs)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d19.1.data') == 16
    process('d19.2.data')
