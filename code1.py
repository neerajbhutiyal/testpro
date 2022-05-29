import re
fhand = open("file1.txt")
lst = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1:
        continue
    for val in stuff:
        val = int(val)
        lst.append(val)
print("The Sum of all number in list is:", sum(lst))