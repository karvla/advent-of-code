## advent of code 2024
## https://adventofcode.com/2024
## day 2

def parse_input(lines):
    return [[int(s) for s in l.split()] for l in lines]

def part1(data):
    print(data)
    s = 0
    for l in data:
        print()
        sorted_1 = list(sorted(l))
        sorted_2 = list(reversed(sorted(l)))
        print(sorted_1)
        print(sorted_2)
        if not all([a == s1 or a == s2 for a, s1, s2 in zip(l, sorted_1, sorted_2)]):
            print(1)

            continue

        if not all([l[i] != l[i+1] for i in range(len(l)-1)]):
            print(2, l)
            continue

        if not all([abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1)]):
            print(3, l)
            continue

        s += 1
        print("s", s)
    return s


def part2(data):
    print(data)
    s = 0
    for l1 in data:
        safe = False
        print()
        for index, l in enumerate([l1] + [l1[:f] + l1[f+1:] for f in range(len(l1))], start=1):
            print(l)
            sorted_1 = list(sorted(l))
            sorted_2 = list(reversed(sorted(l)))
            if not all([a == s1 or a == s2 for a, s1, s2 in zip(l, sorted_1, sorted_2)]):
                print("index", index)
                continue

            if not all([l[i] != l[i+1] for i in range(len(l)-1)]):
                print("index", index)
                continue

            if not all([abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1)]):
                continue
            safe = True


        print(safe)
        if safe == True:
            s += 1
    return s
