## advent of code 2024
## https://adventofcode.com/2024
## day 1

def parse_input(lines):
    numbers = [a.split() for a in lines]
    a, b = zip(*[(int(a), int(b)) for a, b in numbers])
    return a, b


def part1(list_a, list_b):
    sorted_a, sorted_b = sorted(list_a), sorted(list_b)
    return sum([
        abs(a - b)
        for a, b in zip(sorted_a, sorted_b)
    ])


def part2(list_a, list_b):
    return sum([
        a * list_b.count(a)
        for a in list_a
    ])
