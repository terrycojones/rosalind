s = 'ACATTACACACGTGCGAACGACATGTGTGGGTATCCCGCTTAGTGCCGCCGAGTGTAGGCC'

# Quick 'n' dirty (and inefficient).
print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))

# Simple.
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for c in s:
    count[c] += 1

print(count['A'], count['C'], count['G'], count['T'])

# Use a defaultdict (this will not fail on non-ACGT input).
from collections import defaultdict

count = defaultdict(int)

for c in s:
    count[c] += 1

print(count['A'], count['C'], count['G'], count['T'])

# Use a Counter (also will not fail on non-ACGT input).
from collections import Counter

count = Counter()

for c in s:
    count[c] += 1

print(count['A'], count['C'], count['G'], count['T'])
