import math
import sys


def fuel_required(mass):
    return math.floor(mass / 3) - 2


def main(infile):
    with open(infile, 'r') as fp:
        print(sum(fuel_required(int(x.strip())) for x in fp if x.strip()))


main(sys.argv[1])
