
def totalSuccesses(step,successes):
    with open('successes.txt', "a+") as successesFile:
            successesFile.write(str(step) + " ")
            successesFile.write(str(successes) + "\n")
    return successes

def totalDifferentWords(step):
    totalDifferentWords = 0
    with open('words.txt', "r") as wordsFile:
        wordsFile.readline()
        for line in wordsFile:
            totalDifferentWords = totalDifferentWords + 1

    with open("totalDifferentWords.txt", "w") as tdf:
        tdf.write(str(step) + " ")
        tdf.write(str(totalDifferentWords) + "\n")
    return totalDifferentWords


def getDifferentWords1D(board):
    differentWords = []
    for x in board:
            for word in x:
                if word in x:
                    if word not in differentWords:
                        differentWords.append(word)
    return differentWords

def getDifferentWords2D(board):
    differentWords = []
    for y in board:
        for x in y:
            for word in x:
                if word in x:
                    if word not in differentWords:
                        differentWords.append(word)
    return differentWords

def updateWordList(words):
    open("words.txt", "w").close()
    with open('words.txt', "a+") as wordsFile:
        for word in words:
                wordsFile.write(word + "\n")
    return 0


def totalWords2D(board, step):
    totalWords = 0
    for y in board:
        for x in y:
            totalWords = totalWords + len(x)
    with open('totalWords.txt', "a+") as totalWordsFile:
            totalWordsFile.write(str(step) + " ")
            totalWordsFile.write(str(totalWords) + "\n")
    return totalWords


def totalWords1D(board, step):
    totalWords = 0
    for x in board:
        totalWords = totalWords + len(x)
    with open('totalWords1D.txt', "a+") as totalWordsFile:
        totalWordsFile.write(str(step) + " ")
        totalWordsFile.write(str(totalWords) + "\n")
    return totalWords
