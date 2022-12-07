with open("input") as f:
    file = f.read()

#file = """
#$ cd /
#$ ls
#dir a
#14848514 b.txt
#8504156 c.dat
#dir d
#$ cd a
#$ ls
#dir e
#29116 f
#2557 g
#62596 h.lst
#$ cd e
#$ ls
#584 i
#$ cd ..
#$ cd ..
#$ cd d
#$ ls
#4060174 j
#8033020 d.log
#5626152 d.ext
#7214296 k
#"""

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

d = {}

from pathlib import Path

current_path = Path("/")

def proccess_lin(l):
    global current_path

    print(l)
    if l.startswith("dir"):
        return

    if l.startswith("$ ls"):
        return

    if l.startswith("$"):
        _, command, arg = l.split(" ")
        if command == "cd":
            current_path /= arg
            current_path = current_path.resolve()

    if is_integer(l.split(" ")[0]):
        size, file = l.split(" ")
        for p in current_path.parents:
            if p in d:
                d[p] += int(size)
            else:
                d[p] = int(size)
        if current_path in d:
            d[current_path] += int(size)
        else:
            d[current_path] = int(size)



for l in file.splitlines():
    proccess_lin(l)

s = 0
for key, value in d.items():
    if value < 100000:
        s += value

print(s)

min_size = 30000000 - (70000000 - d[Path("/")]) 
print(min_size)

for key, value in sorted(list(d.items()), key=lambda item: item[1]):
    if value > min_size:
        print(value)
        break

