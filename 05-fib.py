#!/usr/bin/env python

from sys import argv

# F(n) = F(n-1) + 1 + F(n-1)
# F(n) = 2^n - 1


def solveHanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * solve(n - 1) + 1


def solve(months, litterSize, indent):
    # print('%s%d: solve called with %d' %
    # (' ' * indent, indent, months))
    if months <= 2:
        return 1
    else:
        aliveLastMonth = solve(months - 1, litterSize, indent + 1)
        mature = solve(months - 2, litterSize, indent + 1)
        return aliveLastMonth + (mature * litterSize)


if len(argv) == 3:
    print(solve(int(argv[1]), int(argv[2]), 0))
else:
    print(solveHanoi(int(argv[1])))
