## advent of code 2024
## https://adventofcode.com/2024
## day 8

from itertools import *


def parse_input(lines):
    return {complex(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}


def part1(data):
    antennas = set(v for k, v in data.items() if v != ".")
    a_groups = {t: set(p for p, a in data.items() if a == t) for t in antennas}
    pos = set()
    for t, aa in a_groups.items():
        for (
            a1,
            a2,
        ) in combinations(aa, r=2):
            v = a2 - a1
            p1 = a1 - v
            p2 = a2 + v
            [pos.add(p) for p in [p1, p2] if p in data]

    d = data.copy()
    width = int(max(*map(lambda i: i.real, d.keys()))) + 1
    for y in range(width):
        for x in range(width):
            p = complex(x, y)
            if p in pos:
                c = "#"
            else:
                c = d[p]
    return len(pos)


def part2(data):
    antennas = set(v for k, v in data.items() if v != ".")

    a_groups = {t: set(p for p, a in data.items() if a == t) for t in antennas}
    pos = set()
    for t, aa in a_groups.items():
        for (
            a1,
            a2,
        ) in combinations(aa, r=2):
            for i in range(100):
                v = a2 - a1
                p1 = a1 - v * i
                p2 = a2 + v * i
                [pos.add(p) for p in [p1, p2] if p in data]

    d = data.copy()
    width = int(max(*map(lambda i: i.real, d.keys()))) + 1
    for y in range(width):
        for x in range(width):
            p = complex(x, y)
            if p in pos:
                c = "#"
            else:
                c = d[p]
    return len(pos)
