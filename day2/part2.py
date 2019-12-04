import itertools
import math
import sys


def execute(data):
    pos = 0
    data_len = len(data)
    while pos < data_len:
        op = data[pos]
        if op == 99:
            pos += 1
            break
        elif op == 1:
            data[data[pos + 3]] = data[data[pos + 1]] + data[data[pos + 2]]
            pos += 4
        elif op == 2:
            data[data[pos + 3]] = data[data[pos + 1]] * data[data[pos + 2]]
            pos += 4
    return data


def main(infile):
    with open(infile, 'r') as fp:
        data = [int(x) for x in fp.read().split(',')]

    target = 19690720
    for noun in range(100):
        for verb in range(100):
            ndata = data.copy()
            ndata[1] = noun
            ndata[2] = verb
            execute(ndata)
            print(noun, '&', verb, '=', ndata[0])
            if ndata[0] == target:
               print('answer =', 100 * noun + verb)
               sys.exit(0)

main(sys.argv[1])
