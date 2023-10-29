import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self): # Calls a new object from the class
        super().__init__() # calls the object from the super class
        self.title("Tic-Tac-Toe Game") # titles the window
        self._cells = {} # creates a blank list for the board to populate