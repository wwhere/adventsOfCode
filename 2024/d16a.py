"""Advent of Code specific utilities"""
from aoc_tools import read_lines
import time

START = 'S'
END = 'E'
WALL = '#'
EMPTY = '.'
TURN_90_POINTS = 1000
STEP_POINTS = 1
EAST = 'E'
SOUTH = 'S'
WEST = 'W'
NORTH = 'N'


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos(self):
        return (self.y, self.x)


class Link:
    def __init__(self, a: Node, b: Node, cost: int, facing: str, visited: list[tuple[int, int]]):
        self.a: Node = a
        self.b: Node = b
        self.cost = cost
        self.facing = facing
        self.visited_positions = visited

    def __str__(self):
        return f'from {self.a.pos()} to {self.b.pos()}, facing {self.facing}, cost={self.cost}, visited={self.visited_positions}'

    def __repr__(self):
        return self.__str__()


def get_next_pos(pos, facing: str) -> tuple[int, int]:
    if facing == EAST:
        return (pos[0], pos[1]+1)
    if facing == SOUTH:
        return (pos[0]+1, pos[1])
    if facing == NORTH:
        return (pos[0]-1, pos[1])
    if facing == WEST:
        return (pos[0], pos[1]-1)


def get_next_steps(grid, pos, facing) -> list[tuple[tuple[int, int], str, int]]:
    next_steps = [
        (get_next_pos(pos, EAST), EAST, STEP_POINTS if facing == EAST else TURN_90_POINTS+STEP_POINTS),
        (get_next_pos(pos, SOUTH), SOUTH, STEP_POINTS if facing == SOUTH else TURN_90_POINTS+STEP_POINTS),
        (get_next_pos(pos, WEST), WEST, STEP_POINTS if facing == WEST else TURN_90_POINTS+STEP_POINTS),
        (get_next_pos(pos, NORTH), NORTH, STEP_POINTS if facing == NORTH else TURN_90_POINTS+STEP_POINTS)]

    if facing == SOUTH:
        next_steps.pop(3)
    if facing == EAST:
        next_steps.pop(2)
    if facing == NORTH:
        next_steps.pop(1)
    if facing == WEST:
        next_steps.pop(0)

    next_steps = list(filter(lambda p: not is_wall(grid, p[0]), next_steps))

    return next_steps


def is_wall(grid, pos: tuple[int, int]) -> bool:
    return grid[pos[0]][pos[1]] == WALL


def is_end(grid, pos: tuple[int, int]) -> bool:
    return grid[pos[0]][pos[1]] == END


def get_turn_cost(from_facing, to_facing):
    if from_facing == to_facing:
        return 0
    if (from_facing, to_facing) in [(EAST, WEST), (WEST, EAST), (NORTH, SOUTH), (SOUTH, NORTH)]:
        return 2 * TURN_90_POINTS
    return TURN_90_POINTS


def get_facings(last_facing):
    facings = [EAST, NORTH, SOUTH, WEST]
    if last_facing == SOUTH:
        facings.pop(1)
    if last_facing == EAST:
        facings.pop(3)
    if last_facing == NORTH:
        facings.pop(2)
    if last_facing == WEST:
        facings.pop(0)
    return facings


def find_links(grid, node, current_facing, facings, visited):
    links: list[Link] = []

    for facing in facings:
        cost = get_turn_cost(current_facing, facing)
        first_pos = get_next_pos(node.pos(), facing)
        if is_wall(grid, first_pos):
            continue
        cost += 1
        possible, next_node, next_facing, node_cost = find_node(grid, first_pos, facing)
        if possible and not next_node.pos() in visited:
            cost += node_cost
            new_visited = visited + [node.pos()]
            link = Link(node, next_node, cost, next_facing, new_visited)
            links.append(link)

    return links


def find_node(grid, pos, facing) -> tuple[bool, Node, str, int]:
    cost = 0
    current_pos = pos
    current_facing = facing
    next_steps = get_next_steps(grid, current_pos, facing)

    while len(next_steps) == 1:
        current_pos, current_facing, step_cost = next_steps[0]
        cost += step_cost
        if is_end(grid, current_pos):
            node = Node(current_pos[1], current_pos[0])
            return True, node, current_facing, cost
        next_steps = get_next_steps(grid, current_pos, current_facing)

    if len(next_steps) == 0:
        return False, None, '', cost

    node = Node(current_pos[1], current_pos[0])
    return True, node, current_facing, cost


def get_solution(grid, facing, start, end):
    start_node = Node(start[1], start[0])

    links = find_links(grid, start_node, facing, [EAST, NORTH], [])
    paths_to_nodes = {}

    for l in links:
        paths_to_nodes[l.b.pos()] = l.cost

    while len(links) > 0:
        links.sort(key=lambda l: l.cost, reverse=True)

        # print('Sorted links:')
        # print(links)

        link = links.pop()
        if link.b.pos() == end:
            return link.cost
        facings = get_facings(link.facing)
        next_links = find_links(grid, link.b, link.facing, facings, link.visited_positions)

        for l in next_links:
            l.cost += link.cost
            current_cost_to_node = paths_to_nodes.get(l.b.pos(), -1)
            if current_cost_to_node != -1 and current_cost_to_node + TURN_90_POINTS < l.cost:
                continue
            links.append(l)
            paths_to_nodes[l.b.pos()] = l.cost

    print("Something went wrong, no more links")
    return 0


def process(filename: str) -> int:
    solution = 0
    grid = []
    start_position = (0, 0)
    end_position = (0, 0)
    for line in read_lines(filename):
        row = []
        for c in line:
            if c == START:
                start_position = (len(grid), len(row))
            if c == END:
                end_position = (len(grid), len(row))
            row.append(c)
        grid.append(row)

    solution = get_solution(grid, EAST, start_position, end_position)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d16.4.data') == 2007
    assert process('d16.1.data') == 7036
    assert process('d16.2.data') == 11048
    process('d16.3.data')
