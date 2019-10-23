#!/usr/bin/env python

from sys import argv


def solve(homoDom, hetero, homoRec):
    n = homoDom + hetero + homoRec
    m = n - 1
    return (
        ((homoDom / n) * ((homoDom - 1) / m) * 1.00) +
        ((homoDom / n) * (hetero        / m) * 1.00) +
        ((homoDom / n) * (homoRec       / m) * 1.00) +

        ((hetero  / n) * (homoDom       / m) * 1.00) +
        ((hetero  / n) * ((hetero - 1)  / m) * 0.75) +
        ((hetero  / n) * (homoRec       / m) * 0.50) +

        ((homoRec / n) * (homoDom       / m) * 1.00) +
        ((homoRec / n) * (hetero        / m) * 0.50) +
        ((homoRec / n) * ((homoRec - 1) / m) * 0.00)
    )


assert len(argv) == 4

print(solve(int(argv[1]), int(argv[2]), int(argv[3])))
