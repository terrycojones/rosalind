#!/usr/bin/env python

import sys
from collections import Counter
from Bio import SeqIO

first = True

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    sequence = str(record.seq)
    if first:
        sequenceLen = len(sequence)
        counts = [Counter() for _ in range(sequenceLen)]
        first = False
    else:
        assert len(sequence) == sequenceLen

    for i, nt in enumerate(sequence):
        counts[i][nt] += 1

print(''.join(counts[i].most_common()[0][0]
              for i in range(sequenceLen)))

for nt in 'ACGT':
    print('%s: %s' % (nt, ' '.join(str(counts[i][nt])
                                   for i in range(sequenceLen))))
