import sys


def is_valid(candidate):
    valid = False
    s_cnd = str(candidate)
    t_cnd = len(s_cnd)
    s_cnd += ' '
    for idx in range(1, t_cnd):
        if int(s_cnd[idx]) < int(s_cnd[idx - 1]):
           return False
        if s_cnd[idx] == s_cnd[idx - 1] and s_cnd[idx] != s_cnd[idx + 1]:
           valid = True
    return valid


def main(input):
    input_range = [int(i) for i in input.split('-')]
    print('searching', input_range[0], 'to', input_range[1])
    total = 0
    for candidate in range(*input_range):
        if is_valid(candidate):
            print('found', candidate)
            total += 1
    print('total:', total)


main(sys.argv[1])
