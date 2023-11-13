from normalgame import *
from ticTacToe import *
import math

copiedBoard = [['', '', ''], ['', '', ''], ['', '', '']]
bestMoveR = ''
bestMoveC = ''

def copyBoard():
    for r in copiedBoard:
        for c in copiedBoard:
            copiedBoard[r][c] = TicTacToeBoard.getGameState(r,c)


def spaceAvailable(r, c):
    if TicTacToeBoard.getGameState(r,c) == '':
        return True 
    else:
        return False 
    
def get_possible_moves():
    copyBoard()
    for r in copiedBoard:
        for c in copiedBoard:
            if copiedBoard[r][c] == '':
                copiedBoard[r][c] = computer
                score = minimax(copiedBoard, False)
                copiedBoard[r][c] = ''
                if score > bestScore:
                    bestScore = score
            else:
                copiedBoard[r][c] = ''

def impBotMove():

    bestScore = -800
    r = 0
    c = 0
    for r in copiedBoard:
        for c in copiedBoard:
            if copiedBoard[r][c] == '':
                copiedBoard[r][c] = computer
                score = minimax(copiedBoard, False)
                copiedBoard[r][c] = ''
                if score > bestScore:
                    bestScore = score 
                    bestMoveR = r
                    bestMoveC = c
    TicTacToeBoard.set_game_state(bestMoveR, bestMoveC, computer)
    return 

def minimax(copiedBoard, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1 
    elif checkWhichMarkWon(p1):
        return -1 
    elif checkDraw():
        return 0
    
    if isMaximizing:
        bestScore = -800
        for r in copiedBoard:
            for c in copiedBoard:
                if copiedBoard[r][c] == '':
                    copiedBoard[r][c] = computer 
                    score = minimax(copiedBoard, False)
                    copiedBoard[r][c] = ''
                    if score > bestScore:
                        bestScore = score
        return bestScore 
    else:
        bestScore = 800 
        for r in copiedBoard:
            for c in copiedBoard:
                if copiedBoard[r][c] == '':
                    copiedBoard[r][c] = p1 
                    score = minimax(copiedBoard, True)
                    copiedBoard[r][c] = ''
                    if score < bestScore:
                        bestScore = score 
        return bestScore
    
def checkWhichMarkWon(mark):
    if (copiedBoard[0][0] == copiedBoard[0][1] and copiedBoard[0][0] == copiedBoard[0][2] and copiedBoard[0][0] == mark):
        return True
    elif (copiedBoard[1][0] == copiedBoard[1][1] and copiedBoard[1][0] == copiedBoard[1][2] and copiedBoard[1][0] == mark):
        return True
    elif (copiedBoard[2][0] == copiedBoard[2][1] and copiedBoard[2][0] == copiedBoard[2][2] and copiedBoard[2][0] == mark):
        return True
    elif (copiedBoard[0][0] == copiedBoard[1][0] and copiedBoard[0][0] == copiedBoard[2][0] and copiedBoard[0][0] == mark):
        return True
    elif (copiedBoard[0][1] == copiedBoard[1][1] and copiedBoard[0][1] == copiedBoard[2][1] and copiedBoard[0][1] == mark):
        return True
    elif (copiedBoard[0][2] == copiedBoard[1][2] and copiedBoard[0][2] == copiedBoard[2][2] and copiedBoard[0][2] == mark):
        return True
    elif (copiedBoard[0][0] == copiedBoard[1][1] and copiedBoard[0][0] == copiedBoard[2][2] and copiedBoard[0][0] == mark):
        return True
    elif (copiedBoard[2][0] == copiedBoard[1][1] and copiedBoard[2][0] == copiedBoard[0][2] and copiedBoard[2][0] == mark):
        return True
    else:
        return False
    
def checkDraw():
    for r in copiedBoard:
        for c in copiedBoard:
            if copiedBoard[r][c] == '':
                return False 
        return True