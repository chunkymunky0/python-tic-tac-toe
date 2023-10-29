from gui import *
#from impossibleBot import *
from normalBot import *
from menu import *
from PIL import ImageTk, Image



def main():
    """Create the game's board and run its main loop."""
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()