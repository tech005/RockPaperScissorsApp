from tkinter import *
import random

# root window for game
root = Tk()

# game functions
def gameplay():
    randnum = random.randint(0,2)
    cpudecisions = ["Rock","Paper","Scissors"]
    cpuchoice = cpudecisions[randnum]
    compschoice.set("computer chooses: "+ cpuchoice)
    if (cpuchoice == userchoice):
        gamedecision.set("It's a tie!!")
    elif (cpuchoice == "Paper") and (userchoice == "Scissors"):
        gamedecision.set("You win")
    elif (cpuchoice == "Scissors") and (userchoice == "Rock"):
        gamedecision.set("You win")
    elif (cpuchoice == "Rock") and (userchoice == "Paper"):
        gamedecision.set("You win")
    else:
        gamedecision.set("You lose")
    # print(cpudecisions[randnum])
    # print(userchoice)    

# Functions for setting userchoice on radio button press 
def rockpress():
    global userchoice
    userchoice = "Rock"

def paperpress():
    global userchoice
    userchoice = "Paper"

def scissorpress():
    global userchoice
    userchoice = "Scissors"

# instruction lable
Label(root,text="Rock Papar Scisors game, select an option and hit play \n the computer will randomly choose a selection").pack()

# the 3 options buttons
userchoice = StringVar()
Radiobutton(root, text="Rock", command=rockpress,value=1,indicatoron=0).pack()
Radiobutton(root, text="Paper", command=paperpress,value=2,indicatoron=0).pack()
Radiobutton(root, text="Scissors", command=scissorpress,value=3,indicatoron=0).pack()

# the play button
Button(root, text="Play",command=gameplay).pack()

# computers choice lable
compschoice = StringVar()
compschoice.set("Computers play")
Label(root,textvariable=compschoice).pack()

# outcome lable
gamedecision = StringVar()
gamedecision.set("Ready to play")
Label(root,textvariable=gamedecision).pack()

root.mainloop()
