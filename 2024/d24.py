"""Advent of Code specific utilities"""
import re
from aoc_tools import read_lines


class Gate:
    input_1: str
    operation: str
    input_2: str
    output: str

    def __init__(self, input_1, operation, input_2, output):
        self.input_1 = input_1
        self.operation = operation
        self.input_2 = input_2
        self.output = output

    def __repr__(self):
        return f'{self.input_1} {self.operation} {self.input_2} => {self.output}'

    def __str__(self):
        return self.__repr__()

    def activate(self, wires):
        if self.operation == 'AND':
            wires[self.output] = wires[self.input_1] and wires[self.input_2]
        elif self.operation == 'OR':
            wires[self.output] = wires[self.input_1] or wires[self.input_2]
        elif self.operation == 'XOR':
            wires[self.output] = 1 if wires[self.input_1] != wires[self.input_2] else 0


def extract_binary_value(wires, initial_letter):
    final_wires = [wire for wire in wires if wire.startswith(initial_letter)]
    final_wires.sort(reverse=True)
    values = [str(wires[wire]) for wire in final_wires]

    return int(''.join(values), 2)


def operate_gates(wires: dict, gates: list[Gate]):
    while len(gates) > 0:
        next_gates = []
        for gate in gates:
            if gate.input_1 in wires and gate.input_2 in wires:
                gate.activate(wires)
            else:
                next_gates.append(gate)
        gates = next_gates


def process(filename: str) -> int:
    reading_initial_values = True
    wires = {}
    gates = []
    for line in read_lines(filename):
        if len(line) < 2:
            reading_initial_values = False
            continue
        if reading_initial_values:
            wire, value = line.split(': ')
            wires[wire] = int(value)
        else:
            gates.append(Gate(*re.split(r'\W+', line)))

    operate_gates(wires, gates)

    z_value = extract_binary_value(wires, 'z')

    print(f'{filename}: {z_value}')
    return z_value


def main() -> None:
    assert process('d24.1.data') == 4
    assert process('d24.2.data') == 2024
    process('d24.3.data')


if __name__ == "__main__":
    main()
