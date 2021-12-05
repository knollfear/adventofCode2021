file1 = open('day3.txt', 'r')
Lines = file1.readlines()
print(len(Lines))

result = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in Lines:
    split = list(line)
    print(split)
    for i in range(len(split)-1):
        result[i] += int(split[i])
    print(result)

for r in result:
    if r >= len(Lines)/2:
        print(1)
    else:
        print(0)


