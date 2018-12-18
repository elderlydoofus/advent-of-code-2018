f = open("day-1\\test_input.txt", "r")

freq = 0
seen = False

lines = f.read().splitlines()

for line in f:
    freq += int(line)

print(lines)

f.close()