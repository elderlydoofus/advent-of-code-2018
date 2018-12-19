f = open("day-02\\input.txt", "r")

id_two = 0
id_three = 0

for line in f:
    letters = list(line.rstrip())
    unique_letters = set(line.rstrip())
    id_two_bool = False
    id_three_bool = False
    for letter in unique_letters:
        count = letters.count(letter)
        if count == 2 and id_two_bool == False:
            id_two += 1
            id_two_bool = True
        elif count == 3 and id_three_bool == False:
            id_three += 1
            id_three_bool = True

print(id_two * id_three)