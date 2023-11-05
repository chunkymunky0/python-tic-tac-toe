

    # check_if_tie()
    # if check_if_win() == False:
    #     tie = messagebox.showinfo("tie","its tie")
    #     return tie
def check_if_win():
    global stop_game
    # count = 0
 
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] !=0:
            stop_game = True
 
            winner = messagebox.showinfo("Winner", states[i][0] + " Won")
            # disableAllButton()
            break
 
    # for j in range(3):
        elif states [0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
 
            winner = messagebox.showinfo("Winner", states[0][i]+ " Won!")
            break
 
        elif states[0][0] == states[1][1] == states[2][2] !=0:
            stop_game = True
 
            winner = messagebox.showinfo("Winner", states[0][0]+ " Won!")
            break
 
        elif states[0][2] == states[1][1] == states[2][0] !=0:
            stop_game = True
 
            winner = messagebox.showinfo("Winner" , states[0][2]+ " Won!")
            break
 
        elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
            stop_game = True
 
            winner = messagebox.showinfo("tie", "Tie")