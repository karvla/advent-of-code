with open("input2.txt") as f:
    input = f.read();

rounds = input.splitlines()

def to_int(i):
    if i == "A" or i =="X":
        return 1
    if i == "B" or i =="Y":
        return 2
    if i == "C" or i =="Z":
        return 3

def won(a, b):
    if b == 3 and a == 1:
        return False
    return b > a


def score(e, y):
    e = to_int(e)
    y = to_int(y)

    if (won(e, y)):
        return y + 6
    if e == y:
        return y + 3
    return y

print(score("A", "Y"))
print(score("B", "X"))
print(score("C", "Z"))
print(score("A", "Z"))

print(sum([score(r[0], r[-1]) for r in rounds]))


