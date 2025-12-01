"""Advent of Code specific utilities"""
from collections import defaultdict
from aoc_tools import read_lines


def get_graph(towels):
    start_node = defaultdict(lambda: [])

    for towel in towels:
        first = towel[:1]
        start_node[first] = start_node[first] + [towel]

    return start_node


def is_possible(design, graph, positive_cache, negative_cache):
    if design in positive_cache:
        return True
    if design in negative_cache:
        return False
    first = design[:1]

    if design in graph[first]:
        positive_cache.append(design)
        return True

    for towel in graph[first]:
        if design.startswith(towel):
            if is_possible(design[len(towel):], graph, positive_cache, negative_cache):
                positive_cache.append(design)
                return True

    negative_cache.append(design)
    return False


def solve(towels: list[str], designs: list[str]):
    total = 0
    positive_cache = []
    negative_cache = []

    graph = get_graph(towels)
    for design in designs:
        total += 1 if is_possible(design, graph, positive_cache, negative_cache) else 0

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

        designs.append(line)

    solution = solve(towels, designs)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d19.1.data') == 6
    process('d19.2.data')
