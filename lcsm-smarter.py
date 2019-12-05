#!/usr/bin/env python

# $ time lcsm-smarter.py lcsm.fasta
# GGTTATACCTGTGGAATCTAGAGACGCGCACGGGGAAGGAGCGAGTCGGGCTCCCAAGAAAGGCAGTGGCACACATCCCTTCTATC
# 21.58user 0.01system 0:21.60elapsed

import sys
from Bio import SeqIO


def getSubstrings(s, n):
    """
    Get all substrings of s of length n, if any.
    """
    result = set()
    for start in range(len(s)):
        substring = s[start:start+n]
        if len(substring) != n:
            break
        result.add(substring)
    return result


sequences = set()

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    sequences.add(str(record.seq))

# Or
# sequences = set(str(record.seq)
#                 for record in SeqIO.parse(sys.argv[1], 'fasta'))


length = min(len(s) for s in sequences)

while length > 0:
    first = True
    substrings = set()

    for seq in sequences:
        if first:
            first = False
            substrings = getSubstrings(seq, length)
        else:
            these = getSubstrings(seq, length)
            toRemove = set()
            for s in substrings:
                if s not in these:
                    toRemove.add(s)

            substrings -= toRemove

    if substrings:
        print(substrings.pop())
        break
    else:
        length -= 1

else:
    print('No common substring!')
