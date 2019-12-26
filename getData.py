
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

def getDifferentWords(board2D):
    differentWords = []
    for y in board2D:
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


def totalWords(board2D, step):
    totalWords = 0
    for y in board2D:
        for x in y:
            totalWords = totalWords + len(x)
    with open('totalWords.txt', "a+") as totalWordsFile:
            totalWordsFile.write(str(step) + " ")
            totalWordsFile.write(str(totalWords) + "\n")
    return totalWords
