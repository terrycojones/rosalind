# See https://github.com/acorg/dark-matter/blob/master/dark/aa.py
from dark.aa import CODONS, STOP_CODONS

trans = {}

for aa, codons in CODONS.items():
    for codon in codons:
        trans[codon.replace('T', 'U')] = aa

s = open('07-prot.fasta').read()

stops = [c.replace('T', 'U') for c in STOP_CODONS]

for index in range(0, len(s), 3):
    codon = s[index:index + 3]
    if codon in stops:
        break
    print(trans[codon], end='')

print()
