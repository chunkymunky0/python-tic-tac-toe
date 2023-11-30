from normalGame import *
from ticTacToe import *
import math

class impBot():
    def __init__(self):
        self.copiedBoard = [['', '', ''], ['', '', ''], ['', '', '']]
        self.bestMoveR = ''
        self.bestMoveC = ''

    def copyBoard(self):
        for r in self.copiedBoard:
            for c in self.copiedBoard:
                self.copiedBoard[r][c] = TicTacToeBoard.getGameState(r,c)


    def spaceAvailable(self, r, c):
        if TicTacToeBoard.getGameState(r,c) == '':
            return True 
        else:
            return False 
        
    def get_possible_moves(self):
        self.copyBoard(self)
        for r in self.copiedBoard:
            for c in self.copiedBoard:
                if self.copiedBoard[r][c] == '':
                    self.copiedBoard[r][c] = computer
                    score = self.minimax(self.copiedBoard, False)
                    self.copiedBoard[r][c] = ''
                    if score > bestScore:
                        bestScore = score
                else:
                    self.copiedBoard[r][c] = ''

    def impBotMove(self):

        bestScore = -800
        r = 0
        c = 0
        for r in self.copiedBoard:
            for c in self.copiedBoard:
                if self.copiedBoard[r][c] == '':
                    self.copiedBoard[r][c] = computer
                    score = self.minimax(self.copiedBoard, False)
                    self.copiedBoard[r][c] = ''
                    if score > bestScore:
                        bestScore = score 
                        self.bestMoveR = r
                        self.bestMoveC = c
        TicTacToeBoard.set_game_state(self.bestMoveR, self.bestMoveC, computer)
        return 

    def minimax(self, isMaximizing):
        if self.checkWhichMarkWon(computer):
            return 1 
        elif self.checkWhichMarkWon(p1):
            return -1 
        elif self.checkDraw():
            return 0
        
        if isMaximizing:
            bestScore = -800
            for r in self.copiedBoard:
                for c in self.copiedBoard:
                    if self.copiedBoard[r][c] == '':
                        self.copiedBoard[r][c] = computer 
                        score = self.minimax(self.copiedBoard, False)
                        self.copiedBoard[r][c] = ''
                        if score > bestScore:
                            bestScore = score
            return bestScore 
        else:
            bestScore = 800 
            for r in self.copiedBoard:
                for c in self.copiedBoard:
                    if self.copiedBoard[r][c] == '':
                        self.copiedBoard[r][c] = p1 
                        score = self.minimax(self.copiedBoard, True)
                        self.copiedBoard[r][c] = ''
                        if score < bestScore:
                            bestScore = score 
            return bestScore
        
    def checkWhichMarkWon(self, mark):
        if (self.copiedBoard[0][0] == self.copiedBoard[0][1] and self.copiedBoard[0][0] == self.copiedBoard[0][2] and self.copiedBoard[0][0] == mark):
            return True
        elif (self.copiedBoard[1][0] == self.copiedBoard[1][1] and self.copiedBoard[1][0] == self.copiedBoard[1][2] and self.copiedBoard[1][0] == mark):
            return True
        elif (self.copiedBoard[2][0] == self.copiedBoard[2][1] and self.copiedBoard[2][0] == self.copiedBoard[2][2] and self.copiedBoard[2][0] == mark):
            return True
        elif (self.copiedBoard[0][0] == self.copiedBoard[1][0] and self.copiedBoard[0][0] == self.copiedBoard[2][0] and self.copiedBoard[0][0] == mark):
            return True
        elif (self.copiedBoard[0][1] == self.copiedBoard[1][1] and self.copiedBoard[0][1] == self.copiedBoard[2][1] and self.copiedBoard[0][1] == mark):
            return True
        elif (self.copiedBoard[0][2] == self.copiedBoard[1][2] and self.copiedBoard[0][2] == self.copiedBoard[2][2] and self.copiedBoard[0][2] == mark):
            return True
        elif (self.copiedBoard[0][0] == self.copiedBoard[1][1] and self.copiedBoard[0][0] == self.copiedBoard[2][2] and self.copiedBoard[0][0] == mark):
            return True
        elif (self.copiedBoard[2][0] == self.copiedBoard[1][1] and self.copiedBoard[2][0] == self.copiedBoard[0][2] and self.copiedBoard[2][0] == mark):
            return True
        else:
            return False
        
    def checkDraw(self):
        for r in self.copiedBoard:
            for c in self.copiedBoard:
                if self.copiedBoard[r][c] == '':
                    return False 
            return True