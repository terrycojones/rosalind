# Print all solutions, in a comma-separated list:
print(', '.join(str(i) for i in range(1000, 10000) if str(4 * i) == str(i)[::-1]))

# Just print a list of the solutions:
# print([i for i in range(1000, 10000) if str(4 * i) == str(i)[::-1]])
#
# Or
# print([i for i in range(1000, 10000) if 4 * i == int(str(i)[::-1])])

# Note that 21978, 219978, 219978, 2199978... etc are also solutions.
