from gui import *
from impossibleBot import *
from normalBot import *

# used for bot algorithms
def minimax(board, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1 
    elif checkWhichMarkWon(player):
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

def main():
    """Create the game's board and run its main loop."""
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()