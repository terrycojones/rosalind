#!/usr/bin/env python

import sys
from Bio import SeqIO
from os.path import exists

from dark.aa import CODONS

START_CODON = 'ATG'
STOP_CODONS = {'TAA', 'TAG', 'TGA'}
CODON_TO_AA = {}

START_AA = 'M'
STOP_AA = '*'

for aa, codons in CODONS.items():
    for codon in codons:
        CODON_TO_AA[codon] = aa

for codon in STOP_CODONS:
    CODON_TO_AA[codon] = STOP_AA

_rcTable = str.maketrans('ACGT', 'TGCA')


def revcomp(s):
    """
    Reverse complement a nucleotide string.
    """
    return s.translate(_rcTable)[::-1]


def translate(s):
    """
    Translate nucleotides to AAs.
    """
    result = ''
    for offset in range(0, len(s) - 2, 3):
        codon = s[offset:offset + 3]
        result += CODON_TO_AA[codon]
    return result


def orfs(s):
    """
    Find all ORFs in an AA string.
    """
    slen = len(s)
    offset = 0

    while offset < slen:
        startIndex = s.find(START_AA, offset)
        if startIndex == -1:
            break

        stopIndex = s.find(STOP_AA, startIndex)
        if stopIndex == -1:
            break

        yield s[startIndex:stopIndex]
        offset = startIndex + 1


def allOrfs(s):
    """
    Find all distinct ORFs in all translations of a nucleotide string,
    both in the forward strand and in the reverse complement.
    """
    results = set()

    for seq in s, revcomp(s):
        for suffix in seq, seq[1:], seq[2:]:
            for orf in orfs(translate(suffix)):
                results.add(orf)

    return results


if len(sys.argv) != 2:
    print('I need a filename!', file=sys.stderr)
    sys.exit(1)
else:
    arg = sys.argv[1]
    if exists(arg):
        seq = SeqIO.read(arg, 'fasta')
        sequence = str(seq.seq)
    else:
        sequence = arg
    for orf in sorted(allOrfs(sequence)):
        print(orf)
