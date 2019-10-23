#!/usr/bin/env python

from sys import argv

from Bio import SeqIO


def solve(filename):
    bestId = None
    highestGC = -1.0

    for seq in SeqIO.parse(filename, 'fasta'):
        sequence = str(seq.seq)
        count = 0
        for nt in sequence:
            count += int(nt in 'GC')
        gc = count / len(sequence)
        if gc > highestGC:
            highestGC = gc
            bestId = seq.id

    return bestId, highestGC


assert len(argv) == 2

seqid, gc = solve(argv[1])

print(seqid)
print(gc * 100.0)
