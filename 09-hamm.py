# s1 = 'GATATATGCATATACTT'
# s2 = 'CCTATATGCATATACTT'

with open('09-hamm.txt') as fp:
    s1 = fp.readline().strip()
    s2 = fp.readline().strip()

diffCount = 0
for index in range(len(s1)):
    diffCount += (s1[index] != s2[index])

# Or:
# diffCount = 0
# for a, b in zip(s1, s2):
#     diffCount += (a != b)

# Or:
# diffcount = sum((a != b) for a, b in zip(s1, s2))

print(diffCount)
