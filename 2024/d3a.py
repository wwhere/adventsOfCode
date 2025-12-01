from aoc_tools import read_lines
import re
from functools import reduce
from operator import add

dayData = '3a'
mulOperationRegEx = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')


def process(fileName):
    count = 0
    for line in read_lines(fileName):
        validOperations = mulOperationRegEx.findall(line)
        count += reduce(add, map(lambda op: int(op[0]) * int(op[1]), validOperations))
    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 161
process(f'd{dayData}.data')
