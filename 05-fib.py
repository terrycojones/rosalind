#!/usr/bin/env python

from sys import argv


def solve(months, litterSize, indent):
    # print('%s%d: solve called with %d' %
    # (' ' * indent, indent, months))
    if months <= 2:
        return 1
    else:
        aliveLastMonth = solve(months - 1, litterSize, indent + 1)
        mature = solve(months - 2, litterSize, indent + 1)
        return aliveLastMonth + (mature * litterSize)


print(solve(int(argv[1]), int(argv[2]), 0))
