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


def noObstacle(map, position):
    return not 'O' in map[position[0]][position[1]] and not '^' in map[position[0]][position[1]]


def isOutOfMap(map, position):
    return len(map) <= position[0] or position[0] < 0 or len(map[position[0]]) <= position[1] or position[1] < 0


def obstaclesAllAround(map, p):
    x, y = p
    return x == 0 or map[x-1][y] == '#' \
        and x == len(map)-1 or map[x+1][y] == '#' \
        and y == 0 or map[x][y-1] == '#' \
        and y == len(map[x])-1 or map[x][y+1] == '#'


def possibleObstacle(m, position, direction, initialMap, initialPosition, initialDirection):
    obstaclePosition = calculateStep(position, direction)
    if not isOutOfMap(m, obstaclePosition) and isSpaceFree(m, obstaclePosition) and noObstacle(m, obstaclePosition):
        map = []
        for line in initialMap:
            map.append(line.copy())
        map[obstaclePosition[0]][obstaclePosition[1]] = '#'
        return mapLoops(map, initialPosition, initialDirection), obstaclePosition
    return False, (0, 0)


def mapLoops(map, initialPosition, direction):
    position = initialPosition
    while True:
        nextPosition = calculateStep(position, direction)
        if isOutOfMap(map, nextPosition):
            return False

        while not isSpaceFree(map, nextPosition):
            direction = rotateDirection(direction)
            nextPosition = calculateStep(position, direction)
            if isOutOfMap(map, nextPosition):
                return False

        if direction in map[nextPosition[0]][nextPosition[1]]:
            return True

        map[nextPosition[0]][nextPosition[1]] += direction
        position = nextPosition


def walkMap(map, position, direction, initialPosition, initialDirection):
    inMap = True
    obstacles = {}
    initialMap = []
    for line in map:
        initialMap.append(line.copy())
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

        possible, obstaclePosition = possibleObstacle(
            map, position, direction, initialMap, initialPosition, initialDirection)
        if possible:
            obstacles[f'{obstaclePosition[0]}/{obstaclePosition[1]}'] = True
            map[nextPosition[0]][nextPosition[1]] += 'O'

        if (not direction in map[nextPosition[0]][nextPosition[1]]):
            map[nextPosition[0]][nextPosition[1]] += direction
        position = nextPosition
        continue

    return len(obstacles.keys())


def process(fileName):
    count = 0
    map = []
    guardPosition = (0, 0)
    direction = 'n'
    for line in read_lines(fileName):
        if '^' in line:
            guardPosition = (len(map), line.find('^'))
        map.append(list(line))
        continue
    map[guardPosition[0]][guardPosition[1]] += 'n'
    count = walkMap(map, guardPosition, direction, guardPosition, 'n')

    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 6
process(f'd{dayData}.data')
