with open("input") as f:
    lines = f.read();


def n_chars(line):
    n = 0
    for i in range(len(line)):
        buf = line[i:i+14]
        if (len(set(buf)) ==len(buf)):
            print(buf)
            return i + 14


print(n_chars(lines))
