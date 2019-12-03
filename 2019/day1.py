import math

total = 0

with open("day1.txt") as fp:
    for line in fp:
        mass = int(line.rstrip())
        fuel = mass // 3 - 2
        total += fuel

print(round(total))
