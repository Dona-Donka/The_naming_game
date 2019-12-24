
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

def totalWords(board2D, step):
    totalWords = 0
    for y in board2D:
        for x in y:
            totalWords = totalWords + len(x)
    with open('totalWords.txt', "a+") as totalWordsFile:
            totalWordsFile.write(str(step) + " ")
            totalWordsFile.write(str(totalWords) + "\n")
    return totalWords
