from functools import reduce

with open("input") as f:
    text = f.read()

cycles = 1
x = 1
log = []
for line in text.splitlines():
    op = line.split()
    if len(op) == 1:
        log.append((x, cycles))
        cycles += 1
    else:
        log.append((x, cycles))
        cycles += 1
        log.append((x, cycles))
        cycles += 1
        n = int(op[1])
        x += n

signal = [c * x for c, x in log]
cycle_inx = [20, 60, 100, 140, 180, 220]
signal_of_intereset = [signal[i-1] for i in cycle_inx]
print(signal_of_intereset)
print(sum(signal_of_intereset))

for y in range(6):
    for x in range(40):
        pos = y * 40 + x
        X = log[pos][0]
        if abs(X - pos % 40) < 2:
            print('#', end='')
        else:
            print('.', end='')
    print()


