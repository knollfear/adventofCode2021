PAREN = "()"
SQUARE_BRACE = "[]"
CURLY_BRACE = "{}"
LESS_THAN = "<>"

OPEN = ["(", "[", "{", "<"]
CLOSE = [")", "]", "}", ">"]
SCORE = [3, 57, 1197, 25137]

def getScore(toTest):
    opens = []
    for t in toTest:
        if t in OPEN:
            opens.append(t)
        else:
            closeIndex = CLOSE.index(t)
            openIndex = OPEN.index(opens[-1])
            if openIndex == closeIndex:
                opens.pop()
            else:
                #print("BAD CLOSE ", CLOSE[closeIndex])
                #print("BAD OPEN ", OPEN[openIndex])
                return SCORE[closeIndex]
    return opens

def scoreString(opens):
    score = 0
    for o in opens[::-1]:
        score = 5 * score
        score += OPEN.index(o) + 1

    return score


file1 = open('day10.txt', 'r')
Lines = file1.readlines()
print(len(Lines))
operators = [PAREN, SQUARE_BRACE, CURLY_BRACE, LESS_THAN]
part1 = 0
part2 = []
for line in Lines:
    line = line.replace("\n", "")
    result = getScore(line)
    if type(result) == int:
        part1 += result
    else:
        print(result)
        print(scoreString(result))
        part2.append(scoreString(result))

print(part1)
part2.sort()
print(part2[22])
