import math
import sys


def execute(data):
    pos = 0
    data_len = len(data)
    while pos < data_len:
        op = data[pos]
        if op == 99:
            return data
        elif op == 1:
            data[data[pos + 3]] = data[data[pos + 1]] + data[data[pos + 2]]
        elif op == 2:
            data[data[pos + 3]] = data[data[pos + 1]] * data[data[pos + 2]]
        pos += 4
    raise Exception


def main(infile):
    with open(infile, 'r') as fp:
        data = [int(x) for x in fp.read().split(',')]
        data[1] = 12
        data[2] = 2
        ndata = execute(data.copy())
        print(ndata[0])


main(sys.argv[1])
