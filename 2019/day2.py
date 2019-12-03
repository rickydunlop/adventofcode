import operator

OPCODES = {
    1: operator.add,
    2: operator.mul,
}


with open("day2.txt") as fp:
    data = fp.read()
    values = [int(i) for i in data.split(",")]
    values[1] = 12
    values[2] = 2

    for i in range(0, len(values), 4):
        chunk = values[i : i + 4]
        if chunk[0] in [1, 2]:
            op = OPCODES[chunk[0]]
            values[chunk[3]] = op(values[chunk[1]], values[chunk[2]])
        elif chunk[0] == 99:
            break
    print(",".join([str(x) for x in values]))
