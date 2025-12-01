from collections import defaultdict
from operator import add
from aoc_tools import read_lines

DAY_DATA = '9a'


class Block:
    def __init__(self, is_file: bool, size: int, index: int = 0):
        self._is_file = is_file
        self.size = size
        self._index = index
        self._swapped = False
        self._is_divided = False
        self._blocks: list[Block] = []

    def _str__(self):
        return self.__repr__()

    def __repr__(self):
        output = ''
        if self._is_divided:
            for b in self._blocks:
                output += b.__repr__()
        else:
            # output += f' || {"File" if self._is_file else "Free"} Block size {
            #     self.size} {("File index " + str(self._index)) if self._is_file else ""}'
            output += f'{self._index if self._is_file else "."}' * self.size
        return output

    def copy(self):
        if self._is_divided:
            raise Exception("No copy of divided blocks")
        return Block(self._is_file, self.size, self._index)

    def is_unswapped_file(self):
        return self._is_file and not self._swapped

    def checksum(self, start_at: int) -> int:
        total = 0
        if not self._is_divided:
            if self._is_file:
                for i in range(self.size):
                    total += (start_at + i) * self._index
        else:
            for b in self._blocks:
                total += b.checksum(start_at)
                start_at += b.size
        return total

    def free_space(self):
        if not self._is_divided:
            return 0 if self._is_file else self.size
        else:
            return self._blocks[len(self._blocks)-1].free_space()

    def move_block(self, other):
        new_block: Block = other.copy()
        other._is_file = False
        other._swapped = True
        other._index = 0

        if other.size == self.size:
            self._is_file = True
            self._swapped = True
            self._index = new_block._index
            return

        if self._is_divided:
            self._blocks[len(self._blocks)-1].move_block(new_block)
            return

        self._is_divided = True
        self._blocks.append(new_block)
        empty_space = Block(False, self.size - new_block.size)
        self._blocks.append(empty_space)


def defrag(blocks: list[Block]) -> str:
    for block_index in range(len(blocks)-1, 0, -1):
        if not blocks[block_index].is_unswapped_file():
            continue
        for space_index in range(block_index):
            if blocks[space_index].free_space() >= blocks[block_index].size:
                blocks[space_index].move_block(blocks[block_index])
                break

    return blocks


def checksum(blocks: list) -> int:
    total = 0
    index = 0
    for b in blocks:
        total += b.checksum(index)
        index += b.size
    return total


def process(filename: str) -> int:
    solution = 0
    blocks = []
    size = 0
    file_index = 0
    for line in read_lines(filename):
        is_file = True
        for c in line:
            block_size = int(c)
            blocks.append(Block(is_file, block_size, file_index))
            file_index += 1 if is_file else 0
            size += block_size
            is_file = not is_file
    blocks = defrag(blocks)
    solution = checksum(blocks)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process(f'd{DAY_DATA}.ex.data') == 2858
    process(f'd{DAY_DATA}.data')
