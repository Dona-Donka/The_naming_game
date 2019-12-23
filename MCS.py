import random
import board
import talk
import getData

N_2D = 1000
board2D = board.get2DBoard(N_2D)

def getHearer(x, y):
    randomNumber = random.randint(0, 3)

    if randomNumber == 0:
        if x != 0:
            hearer = board2D[y][x-1]
        else:
            hearer = board2D[y][99]

    if randomNumber == 1:
        if x != 99:
            hearer = board2D[y][x+1]
        else:
            hearer = board2D[y][0]

    if randomNumber == 2:
        if y != 0:
            hearer = board2D[y-1][x]
        else:
            hearer = board2D[9][x]

    if randomNumber == 3:
        if y != 9:
            hearer = board2D[y-1][x]
        else:
            hearer = board2D[0][x]
    return hearer


def MCS(board2D, steps):
    for step in range(steps):
        successes = 0
        for y in range(10):
            for x in range(100):
                speaker = board2D[y][x]
                hearer = getHearer(x, y)
                successes = talk.checkWord(speaker, hearer, successes)
                print(successes)
        print(getData.totalSuccesses(step, successes))
        print(getData.totalWords(board2D))
        print("new: ",getData.totalNewWords())


MCS(board2D,40)
