import Agent

def get2DBoard(N):
    board2D = []
    for y in range(10):
        board2D.append([[] for x in range(100)])
    return(board2D)

def get1DBoard(N):
    return [[N] for x in range(N)]


