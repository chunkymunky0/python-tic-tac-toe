from gui import *
from ticTacToe import *
import math

def spaceAvailable(r, c):
    if [position] == '0':
        return True 
    return False 

def make_best_move():
    bestScore = -math.inf
    bestMove = None
    for move in ticTacBoard.get_possible_moves():
        ticTacBoard.make_move(move)
        score = minimax(False, aiPlayer, ticTacBoard)
        ticTacBoard.undo()
        if (score > bestScore):
            bestScore = score
            bestMove = move
    ticTacBoard.make_move(bestMove)


def impBotMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    insertLetter(computer, bestMove)
    return 

def minimax(board, isMaximizing):
    if checkWhoWon(computer):
        return 1 
    elif checkWhoWon(player):
        return -1 
    elif checkDraw():
        return 0
        
    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer 
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 
    else:
        bestScore = 800 
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player 
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score 
        return bestScore


while not checkWin():
    impBotMove()
    playerMove()