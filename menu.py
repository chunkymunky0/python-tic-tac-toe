from tkinter import *

root = Tk()
root.title("Tic tac toe game Menu")
root.geometry("500x500")

clicked = StringVar()
clicked.set("Tic Tac toe Game")

drop = OptionMenu(root, clicked, "Single player", "Single player impossible bot", "Multiplayer", "Tic tac toe square")
drop.pack()

root.mainloop()
