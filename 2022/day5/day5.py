stacks = [ "VQWMBNZC", "BCWRZH", "JRQF", "TMNFHWSZ", "PQNLWFG", "WPL", "JQCGRDBV", "WBNQZ", "JTGCFLH"]

stacks = [list(s) for s in stacks]
[s.reverse() for s in stacks]

with open("input5.txt") as f:
    lines = f.read().splitlines();

import re

def move(string):
    n, f, t = re.findall(r'\d+', string)
    n = int(n)
    f = int(f)
    t = int(t)

    print([len(s) for s in stacks], string)
    stacks[t-1].extend(stacks[f-1][-n:])
    [stacks[f-1].pop() for n in range(n)]

    #[stacks[t-1].append(stacks[f-1].pop()) for i in range(n)]

[move(l) for l in lines]

print(stacks)
print("".join([s[-1] for s in stacks]))

