"""Modules"""
from numpy import iterable


def read_lines(filename: str):
    """Reads a file line by line

    Args:
        filename (str): The file name

    Yields:
        str: Next line on the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            yield line.replace('\n', '')


def remove_duplicates(l: iterable) -> list:
    """Removes duplicate values from an iterable and returns a list of the remaining

    Args:
        l (iterable): Iterable with values

    Returns:
        list: list of the values without repetitions
    """
    return list(dict.fromkeys(l))
