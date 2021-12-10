def parseLine(line):
    line = line.replace('\n','')
    sides = line.split('->')
    rawParts = [side.split(',') for side in sides]
    parts = [int(x) for x in rawParts]
    return parts

file1 = open('day5.test.txt', 'r')
Lines = file1.readlines()
print(len(Lines))
coords = []
for line in Lines:
    coords.append(parseLine(line))

print(len(coords))
