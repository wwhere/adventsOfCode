from aoc_tools import read_lines

day = "2a"

validRange = range(1, 4)


def process(fileName):
    count = 0
    for report in read_lines(fileName):
        levels = map(int, report.split())
        safe = True
        goingUp = False
        lastLevel = 0
        index = 0
        for index, level in enumerate(levels):
            if index == 0:
                lastLevel = level
                continue
            diff = level - lastLevel
            if index == 1:
                if diff == 0 or abs(diff) not in validRange:
                    safe = False
                    break
                goingUp = diff > 0
                lastLevel = level
                continue
            if diff == 0 or goingUp and diff < 0 or not goingUp and diff > 0 or abs(diff) not in validRange:
                safe = False
                break
            lastLevel = level
        if safe:
            count += 1

    print(f'{fileName}: {count}')
    return count


assert process(f'd{day}.ex.data') == 2
process(f'd{day}.data')
