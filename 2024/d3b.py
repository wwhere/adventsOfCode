from aoc_tools import read_lines
import re
from functools import reduce
from operator import add

dayData = '3b'
mulOperationRegEx = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
doOperation = 'do()'
dontOperation = 'don\'t()'
doOrDoNotRegEx = re.compile(r'(do\(\)|don\'t\(\))')


def process(fileName):
    count = 0
    operationsEnabled = True
    for line in read_lines(fileName):
        splittedLine = doOrDoNotRegEx.split(line)
        for fragment in splittedLine:
            if fragment == doOperation:
                operationsEnabled = True
                continue
            if fragment == dontOperation:
                operationsEnabled = False
                continue
            if operationsEnabled:
                validOperations = mulOperationRegEx.findall(fragment)
                count += reduce(add, map(lambda op: int(op[0]) * int(op[1]), validOperations), 0)
    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 48
process(f'd{dayData}.data')
