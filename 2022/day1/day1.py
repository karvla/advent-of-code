with open("input") as f:
    text = f.read()

gnomes = text.split('\n\n')

def sum_gnome(gnome):
    return sum([int(cal) for cal in gnome.splitlines()])

print(max([sum_gnome(g) for g in gnomes]))

sums = [sum_gnome(g) for g in gnomes]
sums.sort()

print(sum(sums[-3:]))
