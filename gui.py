import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self.configure(bg="#3498db")  # blue
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
                    bg="#ecf0f1"  #light gray
                )
                frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

                label = tk.Label(
                    master=frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="#2c3e50",  # dark gray
                    bg="#ecf0f1"
                )
                label.pack(fill=tk.BOTH, expand=True)

def main():
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
