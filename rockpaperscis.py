# rock paper scissors game with the computer
import random
import time

# dictonary of answers
papsciroc = {1:"paper", 2:"scissors", 3:"rock"}


def computerroll():
    """gives a random paper scissor rock guess"""
    computerroll = random.randint(1, 3)
    return papsciroc[computerroll]

def getuserchoice():
    """takes user input and returns the choice"""
    choices = ["1","2","3"]
    while True:
        choice = input("1 for paper 2 for scissors 3 for rock: ")
        if (choice in choices):
            print(papsciroc[int(choice)],"Nice choice")
            return papsciroc[int(choice)]
        else:
            print("Really?? Try that again. ")

def intro():
    """Game intro screen"""
    print("*************************")
    print("*   Lets play           *")
    print("*     ROCK              *")
    print("*     PAPER             *")
    print("*     SCISSORS          *")
    print("*   Written in python3  *")
    print("*   By Ryan Rogers      *")
    print("*                       *")
    print("*************************")
    print("")

def gamelogic(computerroll, userchoice):
    """takes the user input and computer guess and determines the winner"""
    if (computerroll == userchoice):
        print("It's a tie!!")
    elif (computerroll == papsciroc[1]) and (userchoice == papsciroc[2]):
        print("You win")
    elif (computerroll == papsciroc[2]) and (userchoice == papsciroc[3]):
        print("You win")
    elif (computerroll == papsciroc[3]) and (userchoice == papsciroc[1]):
        print("You win")
    else:
        print("You lose")

def playagain():
    """logic to end or continue the game"""
    while True:
        again = input("Play again? 1 for yes 2 for no: ")
        if (again == "1"):
            return True
        elif(again == "2"):
            return False
        else:
            print("Invalid input! Try again: ") 
        
def main():
    # intro screen
    intro()
    while True:
        # defining the game variables
        computer = computerroll()
        user = getuserchoice()
        print("computer chooses ",computer)
        time.sleep(1)
        # game logic
        gamelogic(computer, user)
        time.sleep(3)
        print("")
        # ending or replaying game
        if (playagain() == True):
            pass
        else:
            print("Goodbye!")
            time.sleep(2)
            break
main()

