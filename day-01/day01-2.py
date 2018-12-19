from itertools import cycle

f = open("day-1\\input.txt", "r")

freq = 0
freq_list = []

for line in cycle(f.read().splitlines()):
    freq += int(line)
    if freq in freq_list:
        print(freq)
        break
    freq_list.append(freq)

f.close()
