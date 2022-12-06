with open("input2.txt") as f:
    input = f.read();

def point(i):
    if i == "A" or i =="X":
        return 1
    if i == "B" or i =="Y":
        return 2
    if i == "C" or i =="Z":
        return 3


def loosing_char(e):
    if e == "A":
        return "Z"
    if e == "B":
        return "X"
    if e == "C":
        return "Y"

def winning_char(e):
    if e == "A":
        return "Y"
    if e == "B":
        return "Z"
    if e == "C":
        return "X"


def fixed(e, y):
    if y =="X":
        return score_rount(e, loosing_char(e))
    if y =="Y":
        return score_rount(e, e)
    if y =="Z":
        return score_rount(e, winning_char(e))



def score_rount(e, y):
    if e == "A" and y =="Y":
        return point(y) + 6
    if e == "B" and y =="Z":
        return point(y) + 6
    if e == "C" and y =="X":
        return point(y) + 6

    if point(e) == point(y):
        return 3 + point(y)

    return point(y)

rounds = input.splitlines()

print(rounds[0][0], rounds[-1][-1])
print(point("Z"))
print([score_rount(r[0], r[-1]) for r in rounds])
print(sum([score_rount(r[0], r[-1]) for r in rounds]))

print(sum([fixed(r[0], r[-1]) for r in rounds]))

