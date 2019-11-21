#!/usr/bin/env python

from sys import argv

# F(n) = F(n-1) + 1 + F(n-1)
# F(n) = 2^n - 1


def solveHanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * solveHanoi(n - 1) + 1

    print(solveHanoi(int(argv[1])))
