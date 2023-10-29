import tkinter
from gameBoardStandard import TicTacToeBoard

# used for bot algorithms
def minimax(board, isMaximizing):
    if checkWhichMarkWon(computer):
        return 1 
    elif checkWhichMarkWon(player):
        return -1 
    elif checkDraw():
        return 0

def main():
    """Create the game's board and run its main loop."""
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()