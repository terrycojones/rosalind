# s = 'GATATATGCATATACTT'
# target = 'ATAT'

with open('08-subs.fasta') as fp:
    s = fp.readline().strip()
    target = fp.readline().strip()

first = True

for index in range(len(s)):
    if s[index:].startswith(target):
        if not first:
            print(' ', end='')
        first = False
        print(index + 1, end='')

print()
