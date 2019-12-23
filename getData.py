
totalSuccesses = 0

def updateTotalSuccesses(successes):
    successes = successes + 1
    return  successes

def totalSuccesses(step,successes):
    with open('successes.txt', "a+") as successesFile:
            successesFile.write(str(step) + " ")
            successesFile.write(str(successes) + "\n")
    return successes

def totalNewWords():
    totalNewWords = 0
    with open('words.txt', "r") as wordsFile:
        wordsFile.readline()
        for line in wordsFile:
            totalNewWords = totalNewWords + 1
    return totalNewWords

def totalWords(board2D):
    totalWords = 0
    for y in board2D:
        for x in y:
            totalWords = totalWords + len(x)
    return totalWords
