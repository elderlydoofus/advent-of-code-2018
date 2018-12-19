f = open("day-02\\test_input.txt", "r")

for line in f:
    letters = list(line.rstrip())
    print(letters)
    for letter in letters:
        if line.count(letter) > 1:
            print("letter " + str(letter) + " has " + str(line.count(letter)) + " occurence(s).")