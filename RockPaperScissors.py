# statement to use random library-folders
import random

cs = [["rock", "paper", "scissors"], ["giant","wizard", "elf"], ["fire", "water", "earth"] ]

def PlayAgain():
    i2 = input("Do you want to play again? (y/n): ")
    if i2 == "y":
        start()
    else:
        exit()


# function to run the game
def Game(decisions):
     # Variable to store empty string
    eString = ""

    # Loop to print out choices on their own line
    for word in decisions:
        # Statement to print out a choice and a new line
      eString = eString + word + " \n"
    # Variable to store user input
    choice = input("Choose one: \n" + eString +"and press enter | return: ")
    # Variable with stated function call to return random integer from 0-2
    cpuChoice = random.randint(0,2)
    # Statement to show the "Ai" generated decision
    print("Computer choice:",decisions[cpuChoice])


    # End game logic

    # Statement to check if user decision equals computer decision
    if choice == decisions[cpuChoice]:
        #return is different than print
        return ("Tie")

    #Variable to  track user choice index
    i = 0
    # Loop to check user choice index in decisions list
    while i < 3:
        # Statement to see if choice matches list value at index
        if choice == decisions[i]:
            choicei = i
        i+=1
        
    if choicei == 2:
        if cpuChoice == 0:
            return ("You have lost this round..")
        if cpuChoice == 1:
            return ("You win this round!")

    elif choicei == 1:
        if cpuChoice == 0:
            return("You win this round!")
        if cpuChoice == 2:
            return("You have lost this round..")

    elif choicei == 0:
        if cpuChoice == 2:
            return("You win this round!")
        if cpuChoice == 1:
            return("You have lost this round..")


    else:
        print("Incorrect input, try again! \n")
        Game(decisions)


def start():
    # Statement to display Game function call with rock paper scissors values
    for e in cs:
        print(e)
    i = input("Choose a rock paper scissor list by entering the first word in the list: ")

    if i == "rock":
        print(Game(cs[0]),"\n")
        PlayAgain()

    if i == "giant":
        print(Game(cs[1]),"\n")
        PlayAgain()

    if i == "fire":
        print(Game(cs[2]),"\n")
        PlayAgain()

if __name__ == '__main__':
    start()
