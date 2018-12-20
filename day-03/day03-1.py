from re import findall

f = open("day-03\\test_input.txt", "r")
contents = f.read().strip().splitlines()

idnum = findall(r"(?<=\#)(\d)", str(contents))
x = findall(r"(?<=\@\s)(\d)", str(contents))
y = findall(r"(?<=\,)(\d)", str(contents))
i = findall(r"(?<=\:\s)(\d)", str(contents))
j = findall(r"(?<=[x])(\d)", str(contents))