#!/usr/bin/env python

from sys import argv

LITTER_SIZE = 1

months = int(argv[1])
lifespan = int(argv[2])
counts = [0, 1, 1]


def aliveIn(month):
    if month < 0:
        return 0
    else:
        return counts[month]


print('months', months, 'lifespan', lifespan)

for month in range(3, months + 1):
    if month > 2:
        die = aliveIn(month - lifespan)
        living = aliveIn(month - 1)
        mature = aliveIn(month - 2)
        born = mature * LITTER_SIZE
        total = living - die + born
        print(f'calculating month {month}: counts={counts[1:]}, '
              f'living={living}, die={die}, mature={mature}, born={born}, '
              f'total={total}.')
        counts.append(total)

# print('finally', counts[1:])
print(counts[-1])
