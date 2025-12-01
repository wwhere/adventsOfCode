"""Advent of Code specific utilities"""
from aoc_tools import read_lines


class Device:
    a = 0
    b = 0
    c = 0
    program = []
    output = []

    def combo(self, operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c

        raise Exception("Bad combo operand")

    def execute(self):
        self.output.clear()

        i = 0
        while i < len(self.program):
            instruction = self.program[i]
            operand = self.program[i+1]
            i = self.execute_instruction(instruction, operand, i)

        return ','.join(self.output)

    def execute_instruction(self, instruction, operand, pointer):
        if instruction == 0:  # adv
            self.a = self.a // pow(2, self.combo(operand))
            return pointer + 2

        if instruction == 1:  # bxl
            self.b = self.b ^ operand
            return pointer + 2

        if instruction == 2:  # bst
            self.b = self.combo(operand) % 8
            return pointer + 2

        if instruction == 3:  # jnz
            if self.a == 0:
                return pointer + 2
            return operand

        if instruction == 4:  # bxc
            self.b = self.b ^ self.c
            return pointer + 2

        if instruction == 5:  # out
            self.output.append(str(self.combo(operand) % 8))
            return pointer + 2

        if instruction == 6:  # bdv
            self.b = self.a // pow(2, self.combo(operand))
            return pointer + 2

        if instruction == 7:  # cdv
            self.c = self.a // pow(2, self.combo(operand))
            return pointer + 2

        raise Exception("Bad instruction")


def process(filename: str) -> int:
    device = Device()

    for line in read_lines(filename):
        if 'Register A:' in line:
            device.a = int(line.replace('Register A: ', ''))
            continue
        if 'Register B:' in line:
            device.b = int(line.replace('Register B: ', ''))
            continue
        if 'Register C:' in line:
            device.c = int(line.replace('Register C: ', ''))
            continue
        if 'Program:' in line:
            device.program = [int(i) for i in line.replace('Program: ', '').split(',')]
            continue

    solution = device.execute()

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d17.1.data') == '4,6,3,5,6,3,5,2,1,0'
    process('d17.2.data')
