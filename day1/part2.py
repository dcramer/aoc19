import math
import sys


def fuel_required(mass):
    fuel = mass
    total = 0
    while fuel > 0:
        fuel = math.floor(fuel / 3) - 2
        if fuel <= 0:
            break
        total += fuel
    return total


def main(infile):
    with open(infile, 'r') as fp:
        print(sum(fuel_required(int(x.strip())) for x in fp if x.strip()))


main(sys.argv[1])
