with open("input4.txt") as f:
    input = f.read()

lines = input.splitlines()


def range_(c):
    a, b = c.split("-")
    return list(range(int(a),int(b) + 1))
    

def contain_other(a, b):
    seta = set(range_(a))
    setb = set(range_(b))


    union = seta.intersection(setb)
    print(union)
    if len(union) == 0:
        return 0
    else:
        return 1
    
print(sum([contain_other(*l.split(",")) for l in lines]))

