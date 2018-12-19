f = open("day-01\\input.txt", "r")

freq = 0

for line in f:
    freq += int(line)

print(freq)

f.close()