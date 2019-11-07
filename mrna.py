# See https://github.com/acorg/dark-matter/blob/master/dark/aa.py
from dark.aa import CODONS, STOP_CODONS

s = 'MLWPNWIEECYCAEFIFPSDQGVCA'

n = 1

for aa in s:
    n *= len(CODONS[aa])
    n %= 1000000

print((n * len(STOP_CODONS)) % 1000000)
