from aoc_tools import read_lines
dayData = "7a"


def process(fileName):
    count = 0
    for line in read_lines(fileName):
        a, b = line.split(': ')
        result = int(a)
        numbers = map(int, b.split(' '))
        totals = [0]
        for n in numbers:
            newTotals = []
            for t in totals:
                if t + n <= result:
                    newTotals.append(t+n)
                if t * n <= result:
                    newTotals.append(t*n)
                if int(f'{t}{n}') <= result:
                    newTotals.append(int(f'{t}{n}'))
            totals = newTotals
        if result in totals:
            count += result

    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 11387
process(f'd{dayData}.data')
