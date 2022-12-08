with open("input") as f:
    m = f.read()

import numpy as np


m = [list(map(int, row)) for row in m.splitlines()]
m = np.array(m)

def is_visible(y, x):
    if x == 0 or x == m.shape[1] - 1:
        return True
    if y == 0 or y == m.shape[0] - 1:
        return True

    h = m[y,x]
    return any([
            all(m[:y,x] < h),
            all(m[y+1:,x] < h),
            all(m[y,:x] < h),
            all(m[y,x+1:] < h),
            ])

from functools import reduce
def scenic_score(y, x):
    if x == 0 or x == m.shape[1] - 1:
        return True
    if y == 0 or y == m.shape[0] - 1:
        return True

    distances = []
    h = m[y,x]
    directions = [list(m[:y,x]),
                  m[y+1:,x],
                  list(m[y,:x]),
                  m[y,x+1:]]

    directions[0].reverse()
    directions[2].reverse()

    for d in directions:
        s = 0
        for i in d:
            s += 1
            if i >= h: break

        distances.append(s)

    return reduce(lambda a, b: a*b, distances)

print(sum([is_visible(y, x) for y, x  in list(zip(*np.where(m > -1)))]))
print(max([scenic_score(y, x) for y, x  in list(zip(*np.where(m > -1)))]))
