import re

f = open("day-03\\test_input.txt", "r")
contents = f.read().strip().splitlines()

idnum = re.findall(r"(?<=\#)(\d)", str(contents))
x = re.findall(r"(?<=\@\s)(\d)", str(contents))
y = re.findall(r"(?<=\,)(\d)", str(contents))
i = re.findall(r"(?<=\:\s)(\d)", str(contents))
j = re.findall(r"(?<=[x])(\d)", str(contents))