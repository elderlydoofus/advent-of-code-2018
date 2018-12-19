f = open("day-02\\test_input.txt", "r")

for line in f:
    for char in list(line.rstrip()):
        print(line.index(char))