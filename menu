from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tic tac toe game Menu")
root.geometry("500x500")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Tic Tac toe Game")


drop = OptionMenu(root, clicked, "Single player", "Single player impossible bot", "Multiplayer", "Tic tac toe square")
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()