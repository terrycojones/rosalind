#!/usr/bin/env python

import sys
from Bio import SeqIO

sequences = []

for record in SeqIO.parse(sys.argv[1], 'fasta'):
    sequences.append((record.id, str(record.seq)))

# Or:
# sequences = [(record.id, str(record.seq)) for
#              record in SeqIO.parse(sys.argv[1], 'fasta')]

for (seqid1, sequence1) in sequences:
    suffix = sequence1[-3:]
    for (seqid2, sequence2) in sequences:
        if seqid1 != seqid2 and suffix == sequence2[:3]:
            print(seqid1, seqid2)
