import tkinter 
from tkinter import messagebox 
  
# Global variables 
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def main(): 
    # initialize global variables 
    global board, winner, counter, X_turn 
    X_turn = True
    winner = None
    counter = 0
    # create the root window 
    root = tkinter.Tk() 
    # create the board frame 
    board = tkinter.Frame(root) 
    board.grid() 
    # create the buttons 
    buttons = create_buttons(board) 
    # create the reset button 
    reset_button = tkinter.Button(root, text = "RESET", 
                                  command = lambda: reset(buttons)) 
    reset_button.grid() 
    # start the game 
    root.mainloop() 


def create_buttons(board): 
    # create 9 buttons 
    buttons = []
    for row in range(3):
        for col in range(3):
            button = tkinter.Button(board, text = EMPTY, 
                                    font = ("Verdana 20 bold"), 
                                    height = 4, width = 8, 
                                    command = lambda row = row, col = col: button_click(row, col, buttons)) 
            button.grid(row = row, column = col) 
            buttons.append(button)
    return buttons 

def button_click(row, col, buttons): 
    # set the global variables 
    global counter, X_turn, winner 
    # if no winner and counter is less than 9 then play 
    if winner == None and counter < 9: 
        if X_turn == True: 
            text = X 
            buttons[row * 3 + col]["text"] = X 
            X_turn = False
        else: 
            text = O 
            buttons[row * 3 + col]["text"] = O 
            X_turn = True
        counter += 1
        # check for winner 
        if winner_check(buttons, text): 
            winner = text 
            messagebox.showinfo("WINNER", "%s WINS" % winner) 
        elif counter == 8: 
            messagebox.showinfo("TIE", "IT'S A TIE") 

def winner_check(buttons, text): 
    # check for horizontal 
    for row in range(3): 
        if buttons[row * 3]["text"] == text and buttons[row * 3 + 1]["text"] == text and buttons[row * 3 + 2]["text"] == text: 
            return True 
    # check for vertical 
    for col in range(3): 
        if buttons[col]["text"] == text and buttons[col + 3]["text"] == text and buttons[col + 6]["text"] == text: 
            return True 
    # check for diagonal 
    if buttons[0]["text"] == text and buttons[4]["text"] == text and buttons[8]["text"] == text: 
        return True 
    if buttons[2]["text"] == text and buttons[4]["text"] == text and buttons[6]["text"] == text: 
        return True 
    return False

def reset(buttons): 
    global counter, X_turn, winner 
    counter = 0
    X_turn = True
    winner = None
    for button in buttons: 
        button["text"] = EMPTY 


main()