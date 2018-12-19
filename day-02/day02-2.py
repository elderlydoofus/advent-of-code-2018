f = open("day-02\\test_input.txt", "r")

for line in f:
    line_a = line.rstrip()
    for line in f:
        line_b = line.rstrip()
        line_comp = line_a + line_b
        line_set = set(line_comp)
        print(line_set)