import tkinter as tk
from tkinter import font
from menu import *
from PIL import ImageTk, Image

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self.configure(bg="#3498db")  # Set the background color to a shade of blue
        
        self._create_board_grid()
        

    def _create_board_grid(self):
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=150)
            for col in range(3):
                self.columnconfigure(col, weight=1, minsize=150)

                frame = tk.Frame(
                    master=self,
                    relief=tk.RAISED,
                    borderwidth=1,
                    bg="#ecf0f1"  # Set the background color of the squares to a light gray
                )
                frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

                button = tk.Button(
                    master=frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="#2c3e50",  # Set the text color to a dark gray
                    bg="#ecf0f1"  # Set the background color of the buttons to match the squares
                )
                button.pack(fill=tk.BOTH, expand=True)

                # Bind a callback function (click_button) to the button click event
                button.bind("<Button-1>", self.click_button)

    def click_button():
        pass
