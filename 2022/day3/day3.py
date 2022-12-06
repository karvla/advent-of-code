with open("input3.txt") as f:
    input = f.read()

lines = input.splitlines()

def prio(char):
    if (char.isupper()):
        return ord(char) - ord("A") + 27

    return ord(char) - ord("a") + 1
print(prio("A"))
print(prio("a"))



def prio_line(line):
    print(line)
    a = line[:len(line) // 2]
    b = line[len(line) // 2:]
    assert len(a) == len(b)

    common = set(a).intersection(set(b)).pop()
    
    return prio(common)

def prio_group(g):
    assert len(g) == 3
    a, b, c = g

    print(a)
    print(b)
    print(c)
    common = set(a).intersection(set(b)).intersection(set(c))
    print(common)
    if len(common):
        return prio(common.pop())

    return 0


#s = sum([prio_line(l) for l in lines])


s = 0
for i in range(len(lines) //3):
    print(i)
    s += prio_group(lines[i*3:i*3+3])


print(s)

