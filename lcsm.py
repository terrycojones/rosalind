#!/usr/bin/env python

# This is simplistic and memory intensive!  An easy way to make it faster
# (but still very naive) would be to work down from the longest possible
# substring length. See lcsm-smarter.py for that approach (a bit faster and
# definitely using less memory).

# $ time lcsm.py lcsm.fasta
# GGTTATACCTGTGGAATCTAGAGACGCGCACGGGGAAGGAGCGAGTCGGGCTCCCAAGAAAGGCAGTGGCACACATCCCTTCTATC
# 26.16user 0.52system 0:26.69elapsed


import sys
from Bio import SeqIO


def getSubstrings(s):
    result = set()
    for start in range(len(s)):
        for stop in range(start + 1, len(s)):
            result.add(s[start:stop])
    return result


first = True
substrings = set()

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    seq = str(record.seq)
    if first:
        first = False
        substrings = getSubstrings(seq)
    else:
        these = getSubstrings(seq)
        toRemove = set()
        for s in substrings:
            if s not in these:
                toRemove.add(s)

        substrings -= toRemove

if substrings:
    maxLen = 0
    longestSeq = None
    for s in substrings:
        if len(s) > maxLen:
            maxLen = len(s)
            longestSeq = s
    print(longestSeq)
else:
    print('No common substring!')
