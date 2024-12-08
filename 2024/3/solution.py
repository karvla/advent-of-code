## advent of code 2024
## https://adventofcode.com/2024
## day 3
import re

def parse_input(lines):
    return "".join(lines)


def part1(data):
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", data))


def part2(data):
    data = data.replace("\n", "") + "do()"
    data = re.sub("don't().*?do()","",data)
    return part1(data)


