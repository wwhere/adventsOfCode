# NOT A COMPLETE SOLUTION!
# THIS JUST HELPS GIVING INFORMATION ABOUT WHERE THE PROBLEMS ARE
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

    def activate(self, wires) -> tuple[str, int]:
        if self.operation == 'AND':
            wires[self.output] = wires[self.input_1] and wires[self.input_2]
        elif self.operation == 'OR':
            wires[self.output] = wires[self.input_1] or wires[self.input_2]
        else:
            wires[self.output] = 1 if wires[self.input_1] != wires[self.input_2] else 0
        return (self.output, wires[self.output])

    def level(self, wires_levels) -> int:
        return max(wires_levels[self.input_1], wires_levels[self.input_2], wires_levels[self.output])


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


def list_gates(wires, g: list[Gate]):
    wires_levels = {}
    sorted_gates = []

    for wire in wires:
        level = int(wire[1:])
        wires_levels[wire] = level

    gates = list(g)

    while len(gates) > 0:
        next_gates = []
        for gate in gates:
            if gate.input_1 in wires_levels and gate.input_2 in wires_levels:
                if 'z' in gate.output:
                    wires_levels[gate.output] = int(gate.output[1:])
                else:
                    wires_levels[gate.output] = max(wires_levels[gate.input_1], wires_levels[gate.input_2])
            else:
                next_gates.append(gate)
        gates = next_gates

    outputs = ['' for __ in range(46)]

    for gate in g:
        input_level_1 = wires_levels[gate.input_1]
        input_level_2 = wires_levels[gate.input_2]
        output_level = wires_levels[gate.output]
        if input_level_1 < output_level and gate.input_1 not in outputs:
            outputs[input_level_1] = gate.input_1
        if input_level_2 < output_level and gate.input_2 not in outputs:
            outputs[input_level_2] = gate.input_2
        if abs(input_level_1-input_level_2) > 1:
            print(f'Gate {gate} has input 1 {input_level_1} and input 2 {input_level_2} and output {output_level}')
        if 'z' in gate.output:
            z_level = int(gate.output[1:])
            if z_level != output_level:
                print(f'Gate {gate} has output {gate.output} but a level of {output_level}')
            if input_level_1 not in [z_level-1, z_level]:
                print(f'Gate {gate} has input {gate.input_1} of level {input_level_1} but a level of {output_level}')
            if input_level_2 not in [z_level-1, z_level]:
                print(f'Gate {gate} has input {gate.input_2} of level {input_level_2} but a level of {output_level}')

    bits = [[] for __ in range(46)]

    for i in range(46):
        for gate in g:
            if gate.level(wires_levels) == i:
                bits[i].append(gate)

        if i == 0:
            for x in [0, 1]:
                for y in [0, 1]:
                    w = {}
                    w[f'x00'] = x
                    w[f'y00'] = y
                    operate_gates(w, bits[i])
                    result = w[f'z00']
                    carry = w[outputs[i]]
                    if result != x ^ y or carry != x & y:
                        print(f'Level {i} {x}+{y} => {result} / {carry}')
        elif i == 45:
            pass
        elif i < 10:
            for x in [0, 1]:
                for y in [0, 1]:
                    for c in [0, 1]:
                        w = {}
                        w[f'x0{i}'] = x
                        w[f'y0{i}'] = y
                        w[outputs[i-1]] = c
                        operate_gates(w, bits[i])
                        result = w[f'z0{i}']
                        carry = w[outputs[i]]
                        if result != x ^ y ^ c or carry != x & c | y & c | x & y:
                            print(f'Level {i} {x}+{y}+{c} => {result} / {carry}')
        else:
            for x in [0, 1]:
                for y in [0, 1]:
                    for c in [0, 1]:
                        w = {}
                        w[f'x{i}'] = x
                        w[f'y{i}'] = y
                        w[outputs[i-1]] = c
                        operate_gates(w, bits[i])
                        result = w[f'z{i}']
                        carry = w[outputs[i]]
                        if result != x ^ y ^ c or carry != x & c | y & c | x & y:
                            print(f'Level {i} {x}+{y}+{c} => {result} / {carry}')

    for i in [12, 29, 33, 37, 44]:
        print(f'LEVEL {i}')
        for gate in g:
            if gate.level(wires_levels) == i:
                print(gate)


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

    x_value = extract_binary_value(wires, 'x')
    y_value = extract_binary_value(wires, 'y')
    expected_z_value = x_value + y_value

    list_gates(wires, gates)

    operate_gates(wires, gates, expected_z_value)

    z_value = extract_binary_value(wires, 'z')

    print(f'{filename}: {x_value} + {y_value} = {z_value} (expected {expected_z_value})')
    return z_value


def main() -> None:
    # process('d24.4.data') #and
    process('d24.3.data')  # sum


if __name__ == "__main__":
    main()
