from aoc_tools import read_lines
from collections import defaultdict

dayData = "5a"


def isValidPath(graph, pages):
    currentNode = pages[0]

    if (len(pages) != len(list(dict.fromkeys(pages)))):
        print('CICLO')
        return False

    for index, page in enumerate(pages):
        if index == 0:
            continue
        if page in graph and currentNode in graph[page]:
            return False
        if currentNode not in graph.keys():
            return False
        if page in graph[currentNode]:
            currentNode = page
            continue

        found = False
        while not found and not all(map(lambda p: p in pages, graph[currentNode])):
            toRemove = []
            for endPage in graph[currentNode]:
                if endPage == page:
                    currentNode = endPage
                    found = True
                    break

                if endPage not in pages:
                    toRemove.append(endPage)
            if not found:
                for r in toRemove:
                    graph[currentNode].remove(r)
                    if r in graph.keys():
                        graph[currentNode] = list(dict.fromkeys(graph[currentNode] + graph[r]))

        for endPage in graph[currentNode]:
            if endPage == page:
                currentNode = endPage
                found = True
                break

        if not found:
            return False

    return True


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

        if not isValidPath(dict(graph), pages):
            continue

        count += int(pages[len(pages) // 2])

        continue

    print(f'{fileName}: {count}')
    return count


assert process(f'd{dayData}.ex.data') == 143
process(f'd{dayData}.data')
