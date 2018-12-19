from itertools import cycle

f = open("day-1\\test_input.txt", "r")

freq = 0
seen = False

lines = f.read().splitlines()

for line in cycle(lines):
    if freq > 30:
        break
    print(line)
    freq += 1

f.close()