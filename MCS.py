import random
import board
import createWord, getData

N_2D = 1000
board2D = board.get2DBoard(N_2D)

def getHearer(y, x):
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



def MCS(board2D, steps):
    for step in range(steps):
        print(step)
        successes = 0
        for y in range(10):
            for x in range(100):
                speaker = board2D[y][x]
                neighbour = getHearer(y, x)
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

        getData.updateWordList(getData.getDifferentWords(board2D))
        print("successes: ", getData.totalSuccesses(step, successes))
        print("total words: ", getData.totalWords(board2D, step))
        print("new words: ", getData.totalDifferentWords(step))
    return board2D


def runProject(board, mcs):
    print("processing...")
    open("totalDifferentWords.txt", "w").close()
    open("successes.txt", "w").close()
    MCS(board, mcs)

runProject(board2D, 100)