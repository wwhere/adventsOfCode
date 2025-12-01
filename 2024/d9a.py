"""Advent of Code specific utilities"""
from collections import defaultdict
from aoc_tools import read_lines

DAY_DATA = '9a'


def defrag(disk: str, files: defaultdict) -> str:
    """Defrags a string

    Args:
        disk (str): the disk
        files (defaultdict): file indexes for disk positions

    Returns:
        str: the defragged disk
    """
    size = len(disk)
    defragged_disk = ['.'] * size
    end_cursor = size-1
    for i1, v1 in enumerate(disk):
        if i1 > end_cursor:
            defragged_disk[i1] = '.'
            files.pop(i1, None)
            continue
        if v1 != '.':
            defragged_disk[i1] = v1
        else:
            for i2 in range(end_cursor, i1, -1):
                if disk[i2] != '.':
                    defragged_disk[i1] = disk[i2]
                    files[i1] = files[i2]
                    end_cursor = i2-1
                    break
            if i2 in (i1, i1+1):
                break
    return ''.join(defragged_disk)


def checksum(disk: str, files: defaultdict) -> int:
    """Calculates the Checksum

    Args:
        disk (str): a string to calculate checksum
        files (dict): containes the file index for disk positions

    Returns:
        int: the checksum
    """
    checksum_value = 0
    for i, v in enumerate(disk):
        checksum_value += i * files[i] if v != '.' else 0
    return checksum_value


def process(filename: str) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    solution = 0
    disk = ''
    files = defaultdict(lambda: 0)
    file_index = 0
    for line in read_lines(filename):
        is_file = True
        for c in line:
            if is_file:
                for __ in range(int(c)):
                    files[len(disk)] = file_index
                    disk += 'X'
                file_index += 1
            else:
                disk += '.' * int(c)
            is_file = not is_file
        continue
    defragged_disk = defrag(disk, files)
    solution = checksum(defragged_disk, files)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process(f'd{DAY_DATA}.ex.data') == 1928
    process(f'd{DAY_DATA}.data')
