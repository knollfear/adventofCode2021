def  processCard(lines):
    card = []
    for line in lines:
        card.append([int(val) for val in line.replace('\n', '').split()])
    #print(card)
    return card

def updateCard(bingoCard, target):
    newCard = []
    for row in bingoCard:
        newRow = []
        for val in row:
            newRow.append("X" if val == target else val)
        newCard.append(newRow)
    return newCard


def checkWinner(bingoCard):
    # Check Row
    for row in bingoCard:
        hits = 0
        for val in row:
            if val == "X":
                hits += 1
        if hits == 5:
            print("winner on line", row)
            return True

    for i in range(0, 5):
        hits = 0
        for row in bingoCard:
            if row[i] == "X":
                hits += 1
        if hits == 5:
            print("winner on column", i)
            return True

    return False

def removeWinners(bingoCards):
    losingCards = []

    for bingoCard in bingoCards:
        winner = checkWinner(bingoCard)
        if not winner:
            losingCards.append(bingoCard)
    return losingCards

def sumCard(bingoCard):
    sum = 0
    for row in bingoCard:
        for val in row:
            if val != 'X':
                sum += int(val)
    return sum


file1 = open('day4.txt', 'r')
Lines = file1.readlines()
print(len(Lines))

bingoNums = Lines[0].split(",")
print(bingoNums)

bingoCards = []
i = 2
while i < len(Lines):
    bingoCards.append(processCard(Lines[i:i+5]))
    i += 6

for target in bingoNums:
    print(len(bingoCards))
    print(target)
    updatedCards = []
    for bingoCard in bingoCards:
        newCard = updateCard(bingoCard, int(target))
        updatedCards.append(newCard)
    print(updatedCards)

    bingoCards = removeWinners(updatedCards)
    #print(bingoCards)
    if len(bingoCards) == 0:
        winningCard = updatedCards[0]
        print("WINNING CARD")
        print(winningCard)
        print("sum is ", sumCard(winningCard))
        print(target)
        print(int(target) * sumCard(winningCard))
        exit()








