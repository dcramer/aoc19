import itertools
import math
import sys


valid_ops = sorted([1, 2, 3, 4, 99], reverse=True)


def splitop(op):
    op = str(op)
    return int(''.join(op[-2:])), [int(o) for o in op[-3::-1]]


def execute(data, input):
    def instr(offset, params):
        try:
            inst = params[offset - 1]
        except IndexError:
            inst = 0
        return inst

    def param(data, pos, offset, params):
        value = data[pos + offset]
        inst = instr(offset, params)

        if inst == 0:
            try:
                return data[value]
            except IndexError as exc:
                raise Exception(f'Cannot find reference {value}') from exc
        if inst == 1:
            return value
        raise NotImplementedError(f'Invalid instruction: {inst}')

    output = None
    pos = 0
    data_len = len(data)
    while pos < data_len:
        op, params = splitop(data[pos])
        if op == 99:
            pos += 1
            break
        elif op == 1:
            data[data[pos + 3] if instr(3, params) == 0 else pos + 3] = param(data, pos, 1, params) + param(data, pos, 2, params)
            pos += 4
        elif op == 2:
            data[data[pos + 3] if instr(3, params) == 0 else pos + 3] = param(data, pos, 1, params) * param(data, pos, 2, params)
            pos += 4
        elif op == 3:
            data[data[pos + 1] if instr(1, params) == 0 else pos + 1] = input
            pos += 2
        elif op == 4:
            output = param(data, pos, 1, params)
            print('output', output)
            pos += 2
        else:
            raise Exception(f'invalid opcode: {op}')
    return data, output


def main(infile):
    with open(infile, 'r') as fp:
        data = [int(x) for x in fp.read().split(',')]

    input = 1
    _, output = execute(data, input)
    print(output)

main(sys.argv[1])
