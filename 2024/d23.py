"""Advent of Code specific utilities"""
from aoc_tools import read_lines
from collections import defaultdict


def process(filename: str, group_size: int, first_letter: str) -> tuple[int, str]:
    links = defaultdict(lambda: [])
    computers = []

    for line in read_lines(filename):
        a, b = line.split('-')
        links[a].append(b)
        links[b].append(a)
        computers += [a, b]

    potential_computers = set(computers)
    first_letter_computers = {x for x in computers if x.startswith(first_letter)}

    groups = {frozenset([pc, link]) for pc in potential_computers for link in links[pc]}

    size = 2
    last_groups = groups
    size_target_groups = {}
    while len(groups) > 0:
        groups, last_groups = {frozenset([*group, link]) for group in groups for pc in group for link in links[pc]
                               if link not in group if group.issubset(links[link])}, groups
        size += 1
        if size == group_size:
            size_target_groups = {group for group in groups if len(group.intersection(first_letter_computers)) > 0}

    solution_target_size = len(size_target_groups)
    assert len(last_groups) == 1
    lan_party = ','.join(sorted(list(last_groups.pop())))
    print(f'{filename}: {solution_target_size} / {lan_party}')
    return (solution_target_size, lan_party)


def main() -> None:
    assert process('d23.1.data', 3, 't') == (7, 'co,de,ka,ta')
    process('d23.2.data', 3, 't')


if __name__ == "__main__":
    main()
