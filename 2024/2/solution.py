## advent of code 2024
## https://adventofcode.com/2024
## day 02


def parse_input(lines):
    return [list(map(int, l.split())) for l in lines]


def is_safe(list):
    return (
            all(1 <= list[i] - list[i + 1] <= 3 for i in range(len(list) - 1)) or 
            all(1 <= list[i + 1] - list[i] <= 3 for i in range(len(list) - 1))
        )


def is_any_safe(list):
    return is_safe(list) or any(
        is_safe(list[:i] + list[i + 1 :]) for i in range(len(list))
    )


def part1(data):
    return len([1 for l in data if is_safe(l)])


def part2(data):
    return len([1 for l in data if is_any_safe(l)])
