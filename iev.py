#!/usr/bin/env python

import sys

(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa) = map(int, sys.argv[1:])

print(
    AA_AA * 2 * 1.00 +
    AA_Aa * 2 * 1.00 +
    AA_aa * 2 * 1.00 +
    Aa_Aa * 2 * 0.75 +
    Aa_aa * 2 * 0.50 +
    aa_aa * 2 * 0.00
)

# Or
# print(2 * (AA_AA * 1.00 +
#            AA_Aa * 1.00 +
#            AA_aa * 1.00 +
#            Aa_Aa * 0.75 +
#            Aa_aa * 0.50 +
#            aa_aa * 0.00))

# Or
# print(2 * (AA_AA + AA_Aa + AA_aa +
#            Aa_Aa * 0.75 +
#            Aa_aa * 0.50))
