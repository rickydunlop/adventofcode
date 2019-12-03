import math

total = 0

with open("day1.txt") as fp:
    for line in fp:
        mass = int(line.rstrip())
        while True:
            fuel = mass // 3 - 2
            if fuel > 0:
                total += fuel
                mass = fuel
            else:
                break

print(math.floor(total))
