f = open("day-02\\test_input.txt", "r")
contents = f.read().strip().splitlines()

for linex in contents:
    for liney in contents:
        print(set(linex + liney))