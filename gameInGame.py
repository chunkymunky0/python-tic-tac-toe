import tkinter as tk
from tkinter import font, messagebox
from normalGame import *

class BigTicTacToeBoard(tk.Tk):
    def __init__(self, titleName = "Tic-Tac-Toe Game"):
        super().__init__()
        self.title(titleName)
        self.geometry("750x750")
        self.resizable(0,0)
        self.configure(bg="#3498db")  # Set the background color to a shade of blue
        self.player_turn = 'X'  # Initialize the first player's turn as 'X'
        self.game_state = [[['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']],
                           [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']],
                           [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']]]  # Initialize the game state
        self._create_board_grid()
        """
        still needs code to use the opponent parameter
        """
        self._create_menu()  # Create the menu

    def _create_board_grid(self):
        color = "#ECF0F1"
        for row in range(9):
            self.rowconfigure(row, weight=1, minsize=75)
            for col in range(9):
                self.columnconfigure(col, weight=1, minsize=75)

                # adds different colors to different squares
                if row < 3:
                    if col < 3:
                        color = "#B1B4B5"
                    elif col < 6:
                        color = "#ECF0F1"
                    elif col < 9:
                        color = "#B1B4B5"
                elif row < 6:
                    if col < 3:
                        color = "#ECF0F1"
                    elif col < 6:
                        color = "#B1B4B5"
                    elif col < 9:
                        color = "#ECF0F1"
                elif row < 9:
                    if col < 3:
                        color = "#B1B4B5"
                    elif col < 6:
                        color = "#ECF0F1"
                    elif col < 9:
                        color = "#B1B4B5"

                frame = tk.Frame(
                    master=self,
                    relief=tk.RAISED,
                    borderwidth=1,
                    bg= color  # Set the background color of the squares to a light gray
                )
                frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

                button = tk.Button(
                    master=frame,
                    text="",
                    font=font.Font(size=13, weight="bold"),
                    fg="#2c3e50",  # Set the text color to a dark gray
                    bg= color  # Set the background color of the buttons to match the squares
                )
                button.pack(fill=tk.BOTH, expand=True)

                # Bind a callback function (click_button) to the button click event
                button.bind("<Button-1>", lambda event, row=row, col=col: self.click_button(event, row, col))

    def set_title(self, newName):
        self.title(newName)
        self.reset_board(newName)
    
    def get_game_state(self, r, c):
        return self.game_state[r][c]
    
    def set_game_state(self, r, c, value):
        self.game_state[r][c] = value

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

    def reset_board(self, titleName = ""):
        # Reset the game board and state
        self.player_turn = 'X'
        self.game_state = [[['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']],
                           [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']],
                           [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']], [['', '', ''], ['', '', ''], ['', '', '']]]
        for child in self.winfo_children():
            if isinstance(child, tk.Frame):
                for button in child.winfo_children():
                    button.config(text="")
        self.destroy()
        if titleName.startswith("Normal Game"):
            app = TicTacToeBoard(titleName)
        elif titleName.startswith("Game in a Game"):
            app = BigTicTacToeBoard(titleName)
        else:
            app = BigTicTacToeBoard()
        app.mainloop()

    def _create_menu(self):
        menu_bar = tk.Menu(master=self, tearoff="off")
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar, tearoff="off")
        file_menu.add_command(
            label="Play Again",
            command=self.reset_board
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)

        game_modes = tk.Menu(master=menu_bar, tearoff="off")
        one_player = tk.Menu(master=game_modes, tearoff="off")
        two_players = tk.Menu(master=game_modes, tearoff="off")
        normal_bot = tk.Menu(master=one_player, tearoff="off")
        game_modes.add_cascade(label="1 Player", menu=one_player)
        game_modes.add_cascade(label="2 Players", menu=two_players)

        two_players.add_command(
            # Two Players (Normal Game)
            #TicTacToeBoard.set_title(self, "Normal Game - Two Players"),
            label="Normal Game",
            #command=self.reset_board
            command = lambda: BigTicTacToeBoard.set_title(self, "Normal Game - Two Players")
        )
        two_players.add_command(
            # Two Players (Game in a Game)
            #TicTacToeBoard.set_title(self, "Game in a Game - Two Players"),
            label="Game in a Game",
            #command=self.reset_board
            command = lambda: BigTicTacToeBoard.set_title(self, "Game in a Game - Two Players")
        )
        one_player.add_cascade(label="Normal Bot", menu=normal_bot)
        normal_bot.add_command(
            # Single Player (Normal Game - Normal Bot)
            #TicTacToeBoard.set_title(self, "Normal Game - Normal Bot"),
            label="Normal Game",
            #command=self.reset_board
            command = lambda: BigTicTacToeBoard.set_title(self, "Normal Game - Normal Bot")
        )
        normal_bot.add_command(
            # Single Player (Game in a Game - Normal Bot)
            #TicTacToeBoard.set_title(self, "Game in a Game - Normal Bot"),
            label="Game in a Game",
            #command=self.reset_board
            command = lambda: BigTicTacToeBoard.set_title(self, "Game in a Game - Normal Bot")
        )
        one_player.add_command(
            #TicTacToeBoard.set_title(self, "Normal Game - Impossible Bot"),
            # Single Player (Impossible Bot)
            label="Impossible Bot",
            #command=self.reset_board
            command = lambda: BigTicTacToeBoard.set_title(self, "Normal Game - Impossible Bot")
        )
        
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Game Modes", menu=game_modes)

    def click_button(self, event, row, col):
        button = event.widget
        if button.cget("text") == "" and not self.check_for_win('X') and not self.check_for_win('O') and not self.check_for_tie():
            button.config(text=self.player_turn)
            self.game_state[row][col] = self.player_turn

            if self.check_for_win(self.player_turn):
                self.display_message(f"{self.player_turn} wins!")
            elif self.check_for_tie():
                self.display_message("It's a tie!")

            self.player_turn = 'O' if self.player_turn == 'X' else 'X'

if __name__ == "__main__":
    app = BigTicTacToeBoard()
    app.mainloop()
