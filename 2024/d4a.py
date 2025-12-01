from aoc_tools import read_lines
dayData = "4a"


def checkPossibility(grid, startX, startY, xTransformation, yTransformation, desc):
    valid = True
    for i, checkLetter in enumerate('XMAS'):
        x = xTransformation(startX, i)
        y = yTransformation(startY, i)
        if grid[y][x] != checkLetter:
            valid = False
            break
    return valid


def process(fileName):
    count = 0
    gridLines = []
    for line in read_lines(fileName):
        gridLines.append(line)

    for y, line in enumerate(gridLines):
        for x, letter in enumerate(line):
            if letter != 'X':
                continue
            if y >= 3:
                # North
                if checkPossibility(gridLines, x, y, lambda x, i: x, lambda y, i: y-i, 'n'):
                    count += 1

            if y <= len(gridLines)-4:
                # South
                if checkPossibility(gridLines, x, y, lambda x, i: x, lambda y, i: y+i, 's'):
                    count += 1

            if x >= 3:
                # West
                if checkPossibility(gridLines, x, y, lambda x, i: x-i, lambda y, i: y, 'w'):
                    count += 1

            if x <= len(line)-4:
                # East
                if checkPossibility(gridLines, x, y, lambda x, i: x+i, lambda y, i: y, 'e'):
                    count += 1

            if y >= 3 and x >= 3:
                # North West
                if checkPossibility(gridLines, x, y, lambda x, i: x-i, lambda y, i: y-i, 'nw'):
                    count += 1

            if y >= 3 and x <= len(line)-4:
                # North East
                if checkPossibility(gridLines, x, y, lambda x, i: x+i, lambda y, i: y-i, 'ne'):
                    count += 1

            if y <= len(gridLines)-4 and x >= 3:
                # South West
                if checkPossibility(gridLines, x, y, lambda x, i: x-i, lambda y, i: y+i, 'sw'):
                    count += 1

            if y <= len(gridLines)-4 and x <= len(line)-4:
                # South East
                if checkPossibility(gridLines, x, y, lambda x, i: x+i, lambda y, i: y+i, 'se'):
                    count += 1

    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 18
process(f'd{dayData}.data')
