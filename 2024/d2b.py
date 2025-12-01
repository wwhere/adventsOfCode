from aoc_tools import read_lines

day = "2a"

validRange = range(1, 4)


def checkReport(report, skip=False, skipIndex=0):
    levels = map(int, report.split())
    safe = True
    goingUp = False
    lastLevel = 0
    checkAgain = False
    indexesToSkip = (0, 0)
    for index, level in enumerate(levels):
        if skip and skipIndex == index:
            continue
        if index == 0 or index == 1 and skip and skipIndex == 0:
            lastLevel = level
            continue
        diff = level - lastLevel
        if index == 1 or index == 2 and skip and skipIndex < 2:
            if diff == 0 or abs(diff) not in validRange:
                if not skip:
                    checkAgain = True
                    indexesToSkip = (index-1, index)
                    break
                safe = False
                break
            goingUp = diff > 0
            lastLevel = level
            continue
        if diff == 0 or goingUp and diff < 0 or not goingUp and diff > 0 or abs(diff) not in validRange:
            if not skip:
                checkAgain = True
                indexesToSkip = (index-1, index)
                break
            safe = False
            break
        lastLevel = level

    if checkAgain:
        safe = checkReport(report, True, indexesToSkip[0]) or checkReport(
            report, True, indexesToSkip[1]) or checkReport(report, True, 0)

    return safe


def process(fileName):
    count = 0
    for report in read_lines(fileName):

        if checkReport(report):
            count += 1

    print(f'{fileName}: {count}')
    return count


assert process(f'd{day}.ex.data') == 4
process(f'd{day}.data')
