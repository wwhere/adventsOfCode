from aoc_tools import read_lines
dayData = "4a"


def checkPossibility(grid, x, y):
    lookFor = ['M', 'S']
    nw = grid[y-1][x-1]
    ne = grid[y-1][x+1]
    sw = grid[y+1][x-1]
    se = grid[y+1][x+1]

    return all([nw in lookFor, ne in lookFor, sw in lookFor, se in lookFor, nw != se, ne != sw])


def process(fileName):
    count = 0
    gridLines = []
    for line in read_lines(fileName):
        gridLines.append(line)

    for y, line in enumerate(gridLines):
        for x, letter in enumerate(line):
            if letter != 'A':
                continue
            if y >= 1 and y <= len(gridLines)-2 and x >= 1 and x <= len(line)-2:
                if checkPossibility(gridLines, x, y):
                    count += 1

    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 9
process(f'd{dayData}.data')
