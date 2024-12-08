## advent of code 2024
## https://adventofcode.com/2024
## day 7
from itertools import combinations_with_replacement, permutations, combinations, product

def parse_input(lines):
    return [ list(map(str, l.replace(":", "").split())) for l in lines]

def is_equal(result, factors):
    for operators in product(["*", "+"], repeat=len(factors)-1):
        f = list(factors)
        ops = list(operators)
        collector = f.pop(0)
        while len(f) > 0:
            expression = str(collector)  + ops.pop(0) + f.pop(0)
            collector = eval(expression)
            if collector > result:
                break
        if collector == result:
            return result
    return 0

def part1(data):
    pass
    return sum(is_equal(int(d), f) for d, *f in data)

from tqdm import tqdm
def part2(data):
    def is_equal(result, factors):
        factors  = [int(f) for f in factors]
        if int(result) < sum(int(f) for f in factors):
            return  0
        for operators in product(["*", "+", "||"], repeat=len(list(factors))-1):
            f = list(factors)
            ops = list(operators)
            collector = f.pop(0)
            while len(f) > 0:
                op = ops.pop(0)
                factor = f.pop(0)
                if op == "||":
                    collector = int(str(collector) + str(factor))
                elif op == "*":
                    collector *= factor
                elif op == "+":
                    collector += factor
                if collector > result:
                    break
            if collector == result:
                return result
        return 0
    return sum(is_equal(int(d), f) for d, *f in tqdm(data))
