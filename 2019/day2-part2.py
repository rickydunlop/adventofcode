import operator
import itertools


OPCODES = {
    1: operator.add,
    2: operator.mul,
}


def get_input():
    with open("day2.txt") as fp:
        data = fp.read()
        return [int(i) for i in data.split(",")]


def run(noun, verb):
    values = get_input()
    values[1] = noun
    values[2] = verb

    for i in range(0, len(values), 4):
        chunk = values[i : i + 4]
        if chunk[0] in [1, 2]:
            op = OPCODES[chunk[0]]
            values[chunk[3]] = op(values[chunk[1]], values[chunk[2]])
        elif chunk[0] == 99:
            break
    return values[0]


combinations = itertools.permutations(range(0, 100), 2)

for item in list(combinations):
    result = run(item[0], item[1])
    if result == 19690720:
        answer = 100 * item[0] + item[1]
        print(answer)
        break
