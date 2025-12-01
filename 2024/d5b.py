from aoc_tools import read_lines
from collections import defaultdict
from d5a import isValidPath

dayData = "5a"


def findPath(graph, pages):
    keys = list(graph.keys())

    for k in keys:
        if k in pages:
            graph[k] = list(set(graph[k]).intersection(pages))
        else:
            del graph[k]

    sortedPages = sorted(pages, key=lambda n: len(graph[n]) if n in graph else 0)
    return sortedPages


def process(fileName):
    count = 0

    graph = defaultdict(lambda: [])

    readingGraph = True

    for line in read_lines(fileName):
        if len(line) < 2:
            readingGraph = False
            continue

        if readingGraph:
            start, end = line.split('|')
            graph[start].append(end)
            continue

        pages = line.split(',')

        if isValidPath(dict(graph), pages):
            continue

        validPath = findPath(dict(graph), pages)

        count += int(validPath[len(validPath) // 2])

        continue

    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 123
process(f'd{dayData}.data')
