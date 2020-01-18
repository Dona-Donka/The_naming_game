import random
import board
import createWord, getData

N_2D = 1000
N_1D = 1000
board2D = board.get2DBoard(N_2D)
board1D = board.get1DBoard(N_1D)

def getHearer2D(y, x):
    randomNumber = random.randint(0, 3)

    if randomNumber == 0:
        if x != 0:
            return y, x-1
        else:
            return y, 99

    if randomNumber == 1:
        if x != 99:
            return y, x+1
        else:
            return y, 0

    if randomNumber == 2:
        if y != 0:
            return y-1, x
        else:
            return 9, x

    if randomNumber == 3:
        if y != 9:
            return y-1, x
        else:
            return 0, x

def getHearer1D(n, N):
    randomNumber = random.randint(0, 1)

# left
    if randomNumber == 0:
        if n != 0:
            return n-1
        else:
            return N-1
# right
    if randomNumber == 1:
        if n != N-1:
            return n+1
        else:
            return 0

def getHearer2DMF(x,y):
    randomNumberX = random.randint(0, 99)
    randomNumberY = random.randint(0, 9)
    if x == randomNumberX and y == randomNumberY:
        return getHearer2DMF(x,y)
    else:
        return (randomNumberY,randomNumberX)

def getHearer1DMF(n, N):
    randomNumber = random.randint(0, N)
    if n == randomNumber:
        return getHearer1DMF(n)
    else:
        return randomNumber

def MCS_1D(board1D, N, steps):
    for step in range(steps):
        print(step)
        successes = 0
        for n in range(0, N):
                speaker = board1D[n]
                neighbour = getHearer1D(n, N)
                #hearer = getHearer1DMF(n, N)
                hearer = board1D[neighbour]
                #print(speaker)
                if len(speaker) != 0:
                    word = random.choice(speaker)
                    if word in hearer:
                        successes = successes + 1
                        board1D[n] = [word]
                        board1D[neighbour] = [word]
                    else:
                        hearer.append(word)
                else:
                    speaker.append(createWord.getNewWord())

        getData.updateWordList(getData.getDifferentWords1D(board1D))
        print("successes: ", getData.totalSuccesses(step, successes))
        print("total words: ", getData.totalWords1D(board1D, step))
        print("new words: ", getData.totalDifferentWords(step))
    return board2D


def MCS_2D(board2D, steps):
    for step in range(steps):
        print(step)
        successes = 0
        for y in range(10):
            for x in range(100):
                speaker = board2D[y][x]
                neighbour = getHearer2D(y, x)
                #neighbour = getHearer2DMF(y, x)
                hearer = board2D[neighbour[0]][neighbour[1]]
                if len(speaker) != 0:
                    word = random.choice(speaker)
                    if word in hearer:
                        successes = successes + 1
                        board2D[y][x] = [word]
                        board2D[neighbour[0]][neighbour[1]] = [word]
                    else:
                        hearer.append(word)
                else:
                    speaker.append(createWord.getNewWord())

        getData.updateWordList(getData.getDifferentWords2D(board2D))
        print("successes: ", getData.totalSuccesses(step, successes))
        print("total words: ", getData.totalWords2D(board2D, step))
        print("new words: ", getData.totalDifferentWords(step))
    return board2D


def runProject(board1D, N, mcs):
    print("processing...")
    open("totalDifferentWords.txt", "w").close()
    open("successes.txt", "w").close()
    open("totalWords.txt", "w").close()
    open("totalWords1D.txt", "w").close()
    open("words.txt", "w").close()


    MCS_1D(board1D, N, mcs)

runProject(board1D, 1000, 100)