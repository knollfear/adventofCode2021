file1 = open('day2.txt', 'r')
Lines = file1.readlines()
print(len(Lines))

h = 0
depth = 0
aim = 0
for line in Lines:
    if line.startswith('forward'):
        h += int(line.split(" ")[1])
        depth += aim*int(line.split(" ")[1])
    if line.startswith('down'):
        aim += int(line.split(" ")[1])
    if line.startswith('up'):
        aim -= int(line.split(" ")[1])
    print("horizontal:", h)
    print("depth:", depth)
    print("aim:", aim)
print(h)
print(depth)
print(h*depth)

