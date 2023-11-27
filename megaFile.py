import tkinter as tk
from tkinter import font, messagebox
import math

numPlayers = 1
player = 'p1'
p1 = 'X'
p2 = 'O'
stop_game = False
computer = 'O'
gameMode = "norm"

namedTitle = ""
namedOpponent = ""

copiedBoard = [['', '', ''], ['', '', ''], ['', '', '']]
bestMoveR = ''
bestMoveC = ''




# TicTacToeBoard stuff



class TicTacToeBoard(tk.Tk):
    def __init__(self, titleName = "Tic-Tac-Toe Game"):
        super().__init__()
        #namedTitle = titleName
        self.title(titleName)
        self.geometry("750x750")
        self.resizable(0,0)
        self.configure(bg="#3498db")  # Set the background color to a shade of blue
        self.player_turn = 'X'  # Initialize the first player's turn as 'X'
        self.game_state = [['', '', ''], ['', '', ''], ['', '', '']]  # Initialize the game state
        self._create_board_grid()
        """
        still needs code to use the opponent parameter
        """
        self._create_menu()  # Create the menu

    def _create_board_grid(self):
        color = "#ECF0F1"
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=150)
            for col in range(3):
                self.columnconfigure(col, weight=1, minsize=150)

                # adds different colors to different squares
                if row < 1:
                    if col < 1:
                        color = "#B1B4B5"
                    elif col < 2:
                        color = "#ECF0F1"
                    else:
                        color = "#B1B4B5"
                elif row < 2:
                    if col < 1:
                        color = "#ECF0F1"
                    elif col < 2:
                        color = "#B1B4B5"
                    else:
                        color = "#ECF0F1"
                else:
                    if col < 1:
                        color = "#B1B4B5"
                    elif col < 2:
                        color = "#ECF0F1"
                    else:
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
                    font=font.Font(size=36, weight="bold"),
                    fg="#2c3e50",  # Set the text color to a dark gray
                    bg=color  # Set the background color of the buttons to match the squares
                )
                button.pack(fill=tk.BOTH, expand=True)

                # Bind a callback function (click_button) to the button click event
                button.bind("<Button-1>", lambda event, row=row, col=col: self.click_button(event, row, col))
    def get_title(self):
        return namedTitle

    def set_title(self, newName):
        self.title(newName)
        namedTitle = newName
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

    def reset_board(self, titleName = namedTitle):
        # Reset the game board and state
        self.player_turn = 'X'
        self.game_state = [['', '', ''], ['', '', ''], ['', '', '']]
        for child in self.winfo_children():
            if isinstance(child, tk.Frame):
                for button in child.winfo_children():
                    button.config(text="")
        self.destroy()
        if titleName.startswith("Normal Game"):
            app = TicTacToeBoard(titleName)
        #elif titleName.startswith("Game in a Game"):
            #app = BigTicTacToeBoard(titleName)
        else:
            name = self.get_title()
            app = TicTacToeBoard(name)
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
            command = lambda: TicTacToeBoard.set_title(self, "Normal Game - Two Players")
        )
        """two_players.add_command(
            # Two Players (Game in a Game)
            #TicTacToeBoard.set_title(self, "Game in a Game - Two Players"),
            label="Game in a Game",
            #command=self.reset_board
            command = lambda: TicTacToeBoard.set_title(self, "Game in a Game - Two Players")
        )"""
        one_player.add_cascade(label="Normal Bot", menu=normal_bot)
        normal_bot.add_command(
            # Single Player (Normal Game - Normal Bot)
            #TicTacToeBoard.set_title(self, "Normal Game - Normal Bot"),
            label="Normal Game",
            #command=self.reset_board
            command = lambda: TicTacToeBoard.set_title(self, "Normal Game - Normal Bot")
        )
        """normal_bot.add_command(
            # Single Player (Game in a Game - Normal Bot)
            #TicTacToeBoard.set_title(self, "Game in a Game - Normal Bot"),
            label="Game in a Game",
            #command=self.reset_board
            command = lambda: TicTacToeBoard.set_title(self, "Game in a Game - Normal Bot")
        )"""
        one_player.add_command(
            #TicTacToeBoard.set_title(self, "Normal Game - Impossible Bot"),
            # Single Player (Impossible Bot)
            label="Impossible Bot",
            #command=self.reset_board
            command = lambda: TicTacToeBoard.set_title(self, "Normal Game - Impossible Bot")
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





# impossible Bot Stuff


class impBot():
	def copyBoard():
		for r in copiedBoard:
			for c in copiedBoard:
				copiedBoard[r][c] = TicTacToeBoard.getGameState(r,c)


	def spaceAvailable(r, c):
		if TicTacToeBoard.getGameState(r,c) == '':
			return True 
		else:
			return False 
		
	def get_possible_moves():
		impBot.copyBoard()
		for r in copiedBoard:
			for c in copiedBoard:
				if copiedBoard[r][c] == '':
					copiedBoard[r][c] = computer
					score = impBot.minimax(copiedBoard, False)
					copiedBoard[r][c] = ''
					if score > bestScore:
						bestScore = score
				else:
					copiedBoard[r][c] = ''

	def impBotMove():

		bestScore = -800
		r = 0
		c = 0
		for r in copiedBoard:
			for c in copiedBoard:
				if copiedBoard[r][c] == '':
					copiedBoard[r][c] = computer
					score = impBot.minimax(copiedBoard, False)
					copiedBoard[r][c] = ''
					if score > bestScore:
						bestScore = score 
						bestMoveR = r
						bestMoveC = c
		TicTacToeBoard.set_game_state(bestMoveR, bestMoveC, computer)
		return 

	def minimax(copiedBoard, isMaximizing):
		if impBot.checkWhichMarkWon(computer):
			return 1 
		elif impBot.checkWhichMarkWon(p1):
			return -1 
		elif impBot.checkDraw():
			return 0
		
		if isMaximizing:
			bestScore = -800
			for r in copiedBoard:
				for c in copiedBoard:
					if copiedBoard[r][c] == '':
						copiedBoard[r][c] = computer 
						score = impBot.minimax(copiedBoard, False)
						copiedBoard[r][c] = ''
						if score > bestScore:
							bestScore = score
			return bestScore 
		else:
			bestScore = 800 
			for r in copiedBoard:
				for c in copiedBoard:
					if copiedBoard[r][c] == '':
						copiedBoard[r][c] = p1 
						score = impBot.minimax(copiedBoard, True)
						copiedBoard[r][c] = ''
						if score < bestScore:
							bestScore = score 
			return bestScore
		
	def checkWhichMarkWon(mark):
		if (copiedBoard[0][0] == copiedBoard[0][1] and copiedBoard[0][0] == copiedBoard[0][2] and copiedBoard[0][0] == mark):
			return True
		elif (copiedBoard[1][0] == copiedBoard[1][1] and copiedBoard[1][0] == copiedBoard[1][2] and copiedBoard[1][0] == mark):
			return True
		elif (copiedBoard[2][0] == copiedBoard[2][1] and copiedBoard[2][0] == copiedBoard[2][2] and copiedBoard[2][0] == mark):
			return True
		elif (copiedBoard[0][0] == copiedBoard[1][0] and copiedBoard[0][0] == copiedBoard[2][0] and copiedBoard[0][0] == mark):
			return True
		elif (copiedBoard[0][1] == copiedBoard[1][1] and copiedBoard[0][1] == copiedBoard[2][1] and copiedBoard[0][1] == mark):
			return True
		elif (copiedBoard[0][2] == copiedBoard[1][2] and copiedBoard[0][2] == copiedBoard[2][2] and copiedBoard[0][2] == mark):
			return True
		elif (copiedBoard[0][0] == copiedBoard[1][1] and copiedBoard[0][0] == copiedBoard[2][2] and copiedBoard[0][0] == mark):
			return True
		elif (copiedBoard[2][0] == copiedBoard[1][1] and copiedBoard[2][0] == copiedBoard[0][2] and copiedBoard[2][0] == mark):
			return True
		else:
			return False
		
	def checkDraw():
		for r in copiedBoard:
			for c in copiedBoard:
				if copiedBoard[r][c] == '':
					return False 
			return True


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

	def getPlayer():
		return player

	def switchPlayer():
		if numPlayers == 1:
			if impBot.getPlayer() == p1:
				player = computer
			elif impBot.getPlayer() == computer:
				player = p1
		else:
			if impBot.getPlayer() == p1:
				player = p2
			elif impBot.getPlayer() == computer:
				player = p2




# main


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


    impBot.getPlayer()
    impBot.norm_check_if_win()

    if gameMode == "norm":
        #normal game starter
        board = TicTacToeBoard()
        board.mainloop()
    #elif gameMode == "gng":
        #game in game starter
        #board = BigTicTacToeBoard()
        #board.mainloop()

    #game in game starter
    #board = BigTicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()