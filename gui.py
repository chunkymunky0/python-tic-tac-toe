import tkinter as tk
from tkinter import font, messagebox

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self.configure(bg="#3498db")  # Set the background color to a shade of blue
        self.player_turn = 'X'  # Initialize the first player's turn as 'X'
        self.game_state = [['', '', ''], ['', '', ''], ['', '', '']]  # Initialize the game state
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
                button.bind("<Button-1>", lambda event, row=row, col=col: self.click_button(event, row, col))

    def check_for_win(self, player):
        for row in range(3):
            if all(self.game_state[row][col] == player for col in range(3)):
                return True

        for col in range(3):
            if all(self.game_state[row][col] == player for row in range(3)):
                return True

        if all(self.game_state[i][i] == player for i in range(3)) or all(self.game_state[i][2 - i] == player for i in range(3)):
            return True

        return False

    def check_for_tie(self):
        return all(self.game_state[row][col] != '' for row in range(3) for col in range(3))

    def display_message(self, message):
        messagebox.showinfo("Game Over", message)

    def click_button(self, event, row, col):
        button = event.widget  # Get the button that was clicked
        if button.cget("text") == "" and not self.check_for_win('X') and not self.check_for_win('O') and not self.check_for_tie():
            button.config(text=self.player_turn)  # Set the text to the current player's symbol ('X' or 'O')
            # Update the game state
            self.game_state[row][col] = self.player_turn

            if self.check_for_win(self.player_turn):
                self.display_message(f"{self.player_turn} wins!")
            elif self.check_for_tie():
                self.display_message("It's a tie!")

            # After a move, switch to the other player's turn
            self.player_turn = 'O' if self.player_turn == 'X' else 'X'

if __name__ == "__main__":
    app = TicTacToeBoard()
    app.mainloop()
