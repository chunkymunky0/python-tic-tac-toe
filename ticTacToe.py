from normalgame import *
from gameInGame import *
from impossibleBot import *
from normalBot import *
#from menu import *
from normalGame import *
from PIL import ImageTk, Image
from tkinter import *

numPlayers = 1
player = 'p1'
p1 = 'X'
p2 = 'O'
stop_game = False
computer = 'O'
gameMode = "norm"





    # check_if_tie()
    # if norm_check_if_win() == False:
    #     tie = messagebox.showinfo("tie","its tie")
    #     return tie
def norm_check_if_win():
    global stop_game
    states = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
 
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] !=0:
            stop_game = True
 
            #winner = messagebox.showinfo("Winner", states[i][0] + " Won")
            # disableAllButton()
            break
 
    #for j in range(3):
        elif states [0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
 
            #winner = messagebox.showinfo("Winner", states[0][i]+ " Won!")
            break
 
        elif states[0][0] == states[1][1] == states[2][2] !=0:
            stop_game = True
 
            #winner = messagebox.showinfo("Winner", states[0][0]+ " Won!")
            break
 
        elif states[0][2] == states[1][1] == states[2][0] !=0:
            stop_game = True
 
            #winner = messagebox.showinfo("Winner" , states[0][2]+ " Won!")
            break
 
        elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
            stop_game = True
 
            #winner = messagebox.showinfo("tie", "Tie")

def switchPlayer():
    if numPlayers == 1:
        if player == p1:
            player = computer
        elif player == computer:
            player = p1
    else:
        if player == p1:
            player = p2
        elif player == computer:
            player = p2

def getPlayer():
    return player

def main():
    """Create the game's board and run its main loop."""
    """#Button
    b = [
        [0,0,0],
        [0,0,0],
        [0,0,0]]
    
    #text for buttons
    states = [
        [0,0,0],
        [0,0,0],
        [0,0,0]]"""

    if gameMode == "norm":
        #Button
        b = [
            [0,0,0],
            [0,0,0],
            [0,0,0]]
        
        #text for buttons
        states = [
            [0,0,0],
            [0,0,0],
            [0,0,0]]
        
    elif gameMode == "gng":
        #Button
        b = [
            [[0,0,0], [0,0,0], [0,0,0]],
            [[0,0,0], [0,0,0], [0,0,0]],
            [[0,0,0], [0,0,0], [0,0,0]]]
        
        #text for buttons
        states = [
            [[0,0,0], [0,0,0], [0,0,0]],
            [[0,0,0], [0,0,0], [0,0,0]],
            [[0,0,0], [0,0,0], [0,0,0]]]


    getPlayer()
    norm_check_if_win()

    if gameMode == "norm":
        #normal game starter
        board = TicTacToeBoard()
        board.mainloop()
    elif gameMode == "gng":
        #game in game starter
        board = BigTicTacToeBoard()
        board.mainloop()

    #game in game starter
    #board = BigTicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()