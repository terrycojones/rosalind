# I got this wrong on my first attempt:

s = 'CATTCTCATAGCCAAAAAAGTACCATCAAGGT'
d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

print(reversed(s).translate(d))

# Note that you could use s[::-1] instead of reversed(s).

# My code should have been:

s = 'CATTCTCATAGCCAAAAAAGTACCATCAAGGT'
d = {ord('A'): 'T', ord('C'): 'G', ord('G'): 'C', ord('T'): 'A'}

print(reversed(s).translate(d))

# Or, simpler:

s = 'CATTCTCATAGCCAAAAAAGTACCATCAAGGT'

print(reversed(s).translate(str.maketrans('ACGT', 'TGCA')))

# The documentation of str.translate (see
# https://docs.python.org/3/library/stdtypes.html?highlight=str#str.translate
# could be clearer (this is not the first time I've made that mistake).

# Brute force

s = 'CATTCTCATAGCCAAAAAAGTACCATCAAGGT'
d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

for c in s[::-1]:
    print(d[c], end='')
print()
