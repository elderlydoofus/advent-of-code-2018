import itertools

f = open("day-02\\test_input.txt", "r")
contents = f.read().strip().splitlines()

for x, y in itertools.product(contents, contents):
    compare = frozenset(x).difference(frozenset(y))
    if len(compare) == 1:
        print(x)