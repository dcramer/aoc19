import sys


def is_valid(candidate):
    ldigit = None
    valid = False
    for digit in str(candidate):
        if ldigit == digit:
            valid = True
        if ldigit and int(ldigit) > int(digit):
            return False
        ldigit = digit
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
