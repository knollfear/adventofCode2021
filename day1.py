file1 = open('day1.txt', 'r')
Lines = file1.readlines()
print(len(Lines))


def getFrame(index, length):
    if len(Lines) < index + length:
        raise Exception("not enough elements")
    sum = 0
    for j in range(length):
        print('Adding')
        sum += int(Lines[index+j])
    print(sum)
    return sum


count = 0
i = 0
for i in range(len(Lines)):
    try:
        current = getFrame(i, 3)
        next = getFrame(i+1, 3)
        if next > current:
            count += 1
    except:
        pass

print(count)

