"""Advent of Code specific utilities"""
from aoc_tools import read_lines
from typing import NamedTuple
from math import dist
from numpy import concatenate


class Box(NamedTuple):
    x: int
    y: int
    z: int


class Connection(NamedTuple):
    box_a: int
    box_b: int
    distance: float


def process(filename: str, number_of_links: int, circuits_to_count: int) -> int:
    solution = 0
    boxes: list[Box] = []
    box_circuits = dict()
    circuits = dict()
    for line in read_lines(filename):
        [x, y, z] = line.split(',')
        boxes.append(Box(int(x), int(y), int(z)))
        box_circuits[len(boxes)-1] = len(boxes)-1
        circuits[len(boxes)-1] = [len(boxes)-1]

    print(f'File {filename} read')

    connections: list[Connection] = []

    for index_from in range(0, len(boxes)-1):
        for index_to in range(index_from+1, len(boxes)):
            distance = dist(boxes[index_from], boxes[index_to])
            connections.append(Connection(index_from, index_to, distance))

    print(f'Distances calculated')

    connections.sort(key=lambda l: l.distance, reverse=False)

    print(f'Distances sorted')
    # print(connections)

    for c in range(0, number_of_links):
        a = connections[c].box_a
        b = connections[c].box_b
        circuit_a = box_circuits[a]
        circuit_b = box_circuits[b]
        if circuit_b == circuit_a:
            continue
        box_circuits[b] = circuit_a
        new_circuit_a = circuits[circuit_a]
        new_circuit_b = []
        for circuit in circuits[circuit_b]:
            new_circuit_a.append(circuit)
            box_circuits[circuit] = circuit_a
        circuits[circuit_a] = new_circuit_a
        circuits[circuit_b] = new_circuit_b

    circuit_list = list(circuits)
    circuit_list.sort(key=lambda l: len(circuits[l]), reverse=True)

    # print(f'Final circuit list: {circuits}')
    # print(f'Final circuit list: {circuit_list}')
    solution = 1

    for x in range(0, circuits_to_count):
        solution *= len(circuits[circuit_list[x]])

    print(f'{filename}: {solution}')
    return solution


def process_b(filename: str) -> int:
    solution = 0
    boxes: list[Box] = []
    box_circuits = dict()
    circuits = dict()
    for line in read_lines(filename):
        [x, y, z] = line.split(',')
        boxes.append(Box(int(x), int(y), int(z)))
        box_circuits[len(boxes)-1] = len(boxes)-1
        circuits[len(boxes)-1] = [len(boxes)-1]

    print(f'File {filename} read')

    connections: list[Connection] = []

    for index_from in range(0, len(boxes)-1):
        for index_to in range(index_from+1, len(boxes)):
            distance = dist(boxes[index_from], boxes[index_to])
            connections.append(Connection(index_from, index_to, distance))

    print(f'Distances calculated')

    connections.sort(key=lambda l: l.distance, reverse=False)

    print(f'Distances sorted')

    for c in range(0, len(connections)):
        a = connections[c].box_a
        b = connections[c].box_b
        circuit_a = box_circuits[a]
        circuit_b = box_circuits[b]
        if circuit_b == circuit_a:
            continue
        box_circuits[b] = circuit_a
        new_circuit_a = circuits[circuit_a]
        new_circuit_b = []
        for circuit in circuits[circuit_b]:
            new_circuit_a.append(circuit)
            box_circuits[circuit] = circuit_a
        circuits[circuit_a] = new_circuit_a
        circuits[circuit_b] = new_circuit_b
        if len(new_circuit_a) == len(boxes):
            solution = boxes[a].x * boxes[b].x
            print(f'{filename}: {solution}')
            return solution

    print(f'{filename}: Something went wrong')
    return -1


def part_1() -> None:
    assert process('d8a.1.data', 10, 3) == 40
    process('d8a.2.data', 1000, 3)


def part_2() -> None:
    assert process_b('d8a.1.data') == 25272
    process_b('d8a.2.data')
    pass


def main() -> None:
    part_1()
    part_2()


if __name__ == "__main__":
    main()
