f = open("day-02\\test_input.txt", "r")
contents = f.read().strip().splitlines()

for linex in contents:
    for liney in contents:
        if len(set(linex + liney)) == 6:
            match = [x for x in list(linex) if x in list(liney)]
            print(str(match))