import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class frameSwitcher(tk.Tk):

	def __init__(self):

		tk.Tk.__init__(self)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}

		for F in (NormalGame, GameInGame):
			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column = 0, sticky="nsew")

		self.show_frame(NormalGame)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()



class NormalGame(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label =tk.Label(self, text="Normal Game", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Game In a Game", 
					  command=lambda: controller.show_frame(GameInGame))
		button1.pack()

class GameInGame(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label =tk.Label(self, text="Game In a Game", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Normal Game", 
					  command=lambda: controller.show_frame(NormalGame))
		button1.pack()

app = frameSwitcher()
app.mainloop()