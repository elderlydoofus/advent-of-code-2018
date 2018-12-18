import fileinput

f = open("input", "r")

for line in fileinput.input(f):
    print(line)