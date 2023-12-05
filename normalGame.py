import tkinter as tk
from tkinter import font, messagebox
import random

class SplashScreen(tk.Tk):
    def __init__(self, title_name="Tic-Tac-Toe Game"):
        super().__init__()
        self.title_name = title_name
        self.title(title_name)
        self.geometry("750x750")
        self.time = 5
        
        self.resizable(0, 0)
        self.configure(bg="#FFFFFF")

        self.splash_label = tk.Label(self, text="The Game will start in " + str(self.time), font=("Times", 18))
        self.splash_label.pack(side="top", pady=200)

        self.countdown()
        

    def countdown(self):
        if self.time > 0:
            self.time -= 1
            self.splash_label.config(text="The Game will start in " + str(self.time))
            self.after(1000, self.countdown)  
        else:
            self.destroy()
            TicTacToeBoard().mainloop()

class TicTacToeBoard(tk.Tk):
    def __init__(self, title_name="Tic-Tac-Toe Game"):
        super().__init__()
        self.title_name = title_name
        self.title(title_name)
        self.geometry("750x750")
        self.resizable(0, 0)
        self.configure(bg="#3498db")
        self.player_turn = 'X'
        self.game_state = [['', '', ''], ['', '', ''], ['', '', '']]
        self._create_board_grid()
        self._create_menu()


        
        

    def _create_board_grid(self):
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=150)
            for col in range(3):
                self.columnconfigure(col, weight=1, minsize=150)
                color = "#B1B4B5" if (row + col) % 2 == 0 else "#ECF0F1"
                frame = tk.Frame(
                    master=self,
                    relief=tk.RAISED,
                    borderwidth=1,
                    bg=color
                )
                frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

                button = tk.Button(
                    master=frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="#2c3e50",
                    bg=color
                )
                button.pack(fill=tk.BOTH, expand=True)
                button.bind("<Button-1>", lambda event, row=row, col=col: self.click_button(event, row, col))

    def get_title(self):
        return self.title_name

    def set_title(self, new_name):
        self.title_name = new_name
        self.title(new_name)
        self.reset_board()

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

    def reset_board(self):
        self.player_turn = 'X'
        self.game_state = [['', '', ''], ['', '', ''], ['', '', '']]
        for child in self.winfo_children():
            if isinstance(child, tk.Frame):
                for button in child.winfo_children():
                    button.config(text="")

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

        menu_bar.add_cascade(label="File", menu=file_menu)

        game_modes = tk.Menu(master=menu_bar, tearoff="off")
        game_modes.add_command(
            label="Player vs Computer",
            command=lambda: self.set_title("Player vs Computer")
        )
        game_modes.add_command(
            label="Player vs Player",
            command=lambda: self.set_title("Player vs Player")
        )
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

            if not self.check_for_win('X') and not self.check_for_win('O') and not self.check_for_tie() and "Computer" in self.get_title():
                self.computer_move()
            else:
                self.player_turn = 'O' if self.player_turn == 'X' else 'X'

    def computer_move(self):
        empty_spots = [(r, c) for r in range(3) for c in range(3) if self.game_state[r][c] == '']
        if empty_spots:
            r, c = random.choice(empty_spots)
            button = self.winfo_children()[r * 3 + c].winfo_children()[0]
            button.config(text='O')
            self.game_state[r][c] = 'O'

            if self.check_for_win('O'):
                self.display_message("Computer wins!")
            elif self.check_for_tie():
                self.display_message("It's a tie!")

def main_window():
    
    
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    
    
    SplashScreen().mainloop()

    #main_window()
    
