## advent of code 2024
## https://adventofcode.com/2024
## day 4

def parse_input(lines):
    return lines

def part1(data):
    count = 0

    data_transposed = [
        "".join([row[x] for row in data])
        for x in range(len(data[0]))
    ]


    for i, d in enumerate([data, data_transposed]):
        for j, line in enumerate(d):
            count += line.count("XMAS")
            count += line.count("SAMX")

    for i, d in enumerate([data]):
        for y in range(len(d)-3):
            for x in range(len(d[1]) - 3):
                word = d[y][x] + d[y+1][x+1]  + d[y+2][x+2] + d[y+3][x+3]
                if word == "XMAS" or word == "SAMX":
                    count += 1

        for y in range(3, len(d)):
            for x in range(len(d[1]) - 3):
                word = d[y][x] + d[y-1][x+1]  + d[y-2][x+2] + d[y-3][x+3]
                if word == "XMAS" or word == "SAMX":
                    count += 1
    return count 

def part2(data):
    d =  data
    count = 0
    for y in range(len(d)-3):
        for x in range(len(d[1]) - 3):
            word = { d[y][x] , d[y+2][x+2]  , d[y+1][x+1] , d[y+2][x] , d[y][x+2] }
            if word == { "X", "M", "A", "S" }:
                count += 1
    return count
