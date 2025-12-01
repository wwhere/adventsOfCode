from aoc_tools import read_lines
dayData = "6a"


def calculateStep(position, direction):
    match direction:
        case 'n':
            return (position[0]-1, position[1])
        case 's':
            return (position[0]+1, position[1])
        case 'e':
            return (position[0], position[1]+1)
        case 'w':
            return (position[0], position[1]-1)


def rotateDirection(direction):
    match direction:
        case 'n':
            return 'e'
        case 's':
            return 'w'
        case 'e':
            return 's'
        case 'w':
            return 'n'


def isSpaceFree(map, position):
    return map[position[0]][position[1]] != '#'


def isOutOfMap(map, position):
    return len(map) <= position[0] or position[0] < 0 or len(map[position[0]]) <= position[1] or position[1] < 0


def walkMap(m, position, direction):
    inMap = True
    count = 1
    map = m.copy()
    while inMap:
        nextPosition = calculateStep(position, direction)
        if isOutOfMap(map, nextPosition):
            inMap = False
            break

        while not isSpaceFree(map, nextPosition):
            direction = rotateDirection(direction)
            nextPosition = calculateStep(position, direction)
            if isOutOfMap(map, nextPosition):
                inMap = False
                break

        if not inMap:
            break

        if (map[nextPosition[0]][nextPosition[1]] != 'X'):
            map[nextPosition[0]][nextPosition[1]] = 'X'
            count += 1
        position = nextPosition
        continue

    return map, count


def process(fileName):
    count = 0
    map = []
    guardPosition = (0, 0)
    direction = 'n'
    for line in read_lines(fileName):
        if '^' in line:
            guardPosition = (len(map), line.find('^'))
            line = line.replace('^', 'X')
        map.append(list(line))
        continue

    updatedMap, count = walkMap(map, guardPosition, direction)

    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 41
process(f'd{dayData}.data')
