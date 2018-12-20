from itertools import product

f = open("day-02\\input.txt", "r")
contents = f.read().strip().splitlines()
 
for x, y in product(contents, repeat=2):
    diff = [i for i,j in zip(x,y) if i == j]
    if len(y)-len(diff) == 1:
        print("".join(diff))
        break