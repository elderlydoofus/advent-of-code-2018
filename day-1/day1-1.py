f = open("day-1\\input.txt", "r")

freq = 0

for line in f:
    freq += int(line)

print(freq)

f.close()