# Developed for SACCDS APCSP

import random

def Game(decisions):
    eString = ""

    for word in decisions:
      eString = eString + word + " \n"

    choice = input("Choose one: \n" + eString +"\n and press enter | return: ")

    cpuChoice = random.randint(0,2)

    print("Computer choice:",decisions[cpuChoice])
    
    if choice == decisions[cpuChoice]:
        return ("Tie")

    # track user choice index
    i = 0
    while i < 3:
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

rps = ["rock", "paper", "scissors"]
print(Game(rps), "\n")
print(Game(["giant","wizard", "elf"]))
