## advent of code 2024
## https://adventofcode.com/2024
## day 6
import sys
sys.setrecursionlimit(15000)

def parse_input(lines):
    return lines

dirs = {
    "^" : (-1, 0),
    "v" : (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}

turn_order = [
    "^",
    ">",
    "v",
    "<",
]


def next_map_fn(data, pos, visited=False):
    #print_map(data)
    next_map = data
    y, x = pos
    dir = data[y][x]
    assert dir in dirs
    next_y, next_x = y + dirs[dir][0], x + dirs[dir][1]
    if not (0 <= next_y < len(data) and 0 <= next_x < len(data[0])):
        next_map[y][x] = "X"
        return data

    next_tile = data[next_y][next_x]
    if next_tile in "#O":
        next_map[y][x] = turn_order[(turn_order.index(dir) + 1) % 4]
        return  next_map_fn(next_map, (y, x))

    next_map[y][x] = "X" 
    visited = next_map[next_y][next_x] == "X"
    next_map[next_y][next_x] = dir

    return  next_map_fn(next_map, (next_y, next_x), visited)


def part1(data):
    data = [[c for c in r] for r in data]
    x_init, y_init = 0, 0
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c in dirs:
                y_init, x_init = y, x
                break


    data = next_map_fn(data, (y_init, x_init))
    return "\n".join(["".join(r) for r in data]).count("X")



from tqdm import tqdm
def part2(map_string):
    map = { 
        complex(x, y) : c
        for y, row in enumerate(map_string)
        for x, c in enumerate(row)
    }

    init_pos = [k  for k,v in map.items() if v == "^"][0]
    d = 0
    current_pos = init_pos
    offset = [
        -1j ,
        1,
        1j,
        -1,
    ]
    init_path = []

    while current_pos in map:
        if map[current_pos] == "#":
            _, current_pos = init_path.pop()
            d = (d + 1) % 4

        init_path.append((d, current_pos))
        current_pos += offset[d]


    obsticles = set()
    for idx, (d, current_pos) in enumerate(tqdm(init_path[:-1])):
        if current_pos == init_path:
            continue
        m = map.copy()

        _, o_pos = init_path[idx+1]
        m[o_pos] = "#"

        d = 0
        current_pos = init_pos
        visited = set()
        while current_pos in m:
            next_pos = current_pos + offset[d]
            if next_pos in m and m[next_pos] == "#":
                d = (d + 1) % 4
                continue

            current_pos = next_pos
            if (d, current_pos) in visited:
                obsticles.add(o_pos)
                break 
            visited.add((d, current_pos))

    return len(obsticles)


