"""Advent of Code specific utilities"""
from typing import Iterator
from aoc_tools import read_lines
from functools import cache

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'
AVOID = 'X'
ACTIVATE = 'A'

numeric_keypad = {
    AVOID: (0,3),
    ACTIVATE: (2,3),
    '0': (1,3),
    '1': (0,2),
    '2': (1,2),
    '3': (2,2),
    '4': (0,1),
    '5': (1,1),
    '6': (2,1),
    '7': (0,0),
    '8': (1,0),
    '9': (2,0)
}

directional_keypad = {
    AVOID: (0,0),
    ACTIVATE: (2,0),
    UP: (1,0),
    LEFT: (0,1),
    DOWN: (1,1),
    RIGHT: (2,1)
}

NUMERIC_KEYPAD = 'NUMERIC'
DIRECTIONAL_KEYPAD = 'DIRECTIONAL'

def get_keypad(name:str):
    return numeric_keypad if name == NUMERIC_KEYPAD else directional_keypad

def get_move_options(position: tuple[int,int], target: tuple[int, int], avoid: tuple[int, int]) -> Iterator[str]:
    target_x, target_y = target
    x, y = position

    horizontal_move = LEFT if target_x < x else RIGHT
    vertical_move = UP if target_y < y else DOWN
    horizontal_distance = abs(target_x-x)
    vertical_distance = abs(target_y-y)

    if position == target:
        yield ACTIVATE
    elif x == target_x:
        yield vertical_move * vertical_distance + ACTIVATE
    elif y == target_y:
        yield horizontal_move * horizontal_distance + ACTIVATE
    else:
        if (target_x, y) != avoid:
            yield horizontal_move * horizontal_distance + vertical_move * vertical_distance + ACTIVATE
        if (x, target_y) != avoid:
            yield vertical_move * vertical_distance + horizontal_move * horizontal_distance + ACTIVATE


def get_keypad_position(keypad_name: str, value: str) -> tuple[int,int]:
    return get_keypad(keypad_name)[value]

def get_sequences(code: str, keypad_name: str, start_at: str) -> list[list[str]]:
    if code == '':
        return [[]]
    
    position = get_keypad_position(keypad_name, start_at)
    target = get_keypad_position(keypad_name, code[0])
    avoid = get_keypad_position(keypad_name, AVOID)

    sequences = [
        [option, *sequence]
        for option in get_move_options(position, target, avoid)
        for sequence in get_sequences(code[1:], keypad_name, code[0])
    ]
    
    return sequences

@cache
def get_best_sequence_length(code: str, loops: int, keypad_name: str) -> int:
    sequences = get_sequences(code, keypad_name, ACTIVATE)
    if loops == 0:
        return min(sum(len(fragment) for fragment in sequence) for sequence in sequences)
    else:
        return min(sum(get_best_sequence_length(fragment, loops - 1, DIRECTIONAL_KEYPAD) for fragment in sequence) for sequence in sequences)

def process(filename: str, loops: int) -> int:
    solution = sum(int(line[:3]) * get_best_sequence_length(line, loops, NUMERIC_KEYPAD) for line in read_lines(filename))
    print(f'{filename},{loops}: {solution}')
    return solution

def part1() -> None:
    assert process('d21.1.data',2) == 126384
    process('d21.2.data',2)

def part2() -> None:
    process('d21.2.data',25)

def main() -> None:
    part1()
    part2()

if __name__ == "__main__":
    main()


