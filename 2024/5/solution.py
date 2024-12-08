## advent of code 2024
## https://adventofcode.com/2024
## day 5

def parse_input(lines):
    rules_end = lines.index("")
    rules = [tuple(map(int, l.split("|"))) for l in lines[:rules_end]]
    update = [tuple(map(int, l.split(","))) for l in lines[rules_end+1:]]
    return rules, update
    

def part1(rules, updates):
    before_dict = {}
    after_dict = {}
    for before, after in rules:
        if before in before_dict:
            before_dict[before].add(after)
        else:
            before_dict[before] = { after }

        if after in after_dict:
            after_dict[after].add(before)
        else:
            after_dict[after] = { before }

    s = 0
    for u in updates:
        update_is_correct = True
        for index, i in enumerate(u):
            if i in before_dict:
                correct = (
                        all(after in before_dict[i] for after in u[index+1:]) and
                    all(before in after_dict[i] for before in u[:index])

                )
                if not correct:
                    update_is_correct = False
                    break
        if update_is_correct:
            s += u[len(u) // 2]
    return s

from functools import cmp_to_key
def part2(rules, updates):
    before_dict = {}
    after_dict = {}
    for before, after in rules:
        if before in before_dict:
            before_dict[before].add(after)
        else:
            before_dict[before] = { after }

        if after in after_dict:
            after_dict[after].add(before)
        else:
            after_dict[after] = { before }

    s = 0
    for u in updates:
        update_is_correct = True
        for index, i in enumerate(u):
            if i in before_dict:
                correct = (
                        all(after in before_dict[i] for after in u[index+1:]) and
                    all(before in after_dict[i] for before in u[:index])

                )
                if not correct:
                    update_is_correct = False
                    break
        if not update_is_correct:

            def comp(a, b):
                if a in before_dict and b in before_dict[a]:
                    return -1
                if b in before_dict and a in before_dict[b]:
                    return 1
                return 0
            u_sorted = sorted(u, key=cmp_to_key(comp))
            s += u_sorted[len(u) // 2]
    return s 
