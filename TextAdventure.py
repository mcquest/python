"""
Example Text Adventure..
Script Name: TextAdventure.py
Coder Name: Charles 
What happens when the script is run?:
User is given a series of choices and must make decisions
to discover and adapt to their environment
"""
# Import time class to use functions in it 
import time

    #empty print to create new line after statement
    print()

# Introductory decisions
def Welcome():
    # Opening Line
    start = input("You are sitting outside on a bench and it starts to"
                " rain, \n do you want to use your umbrella or go inside? (u/i) : ")
    # Check user response to start with if statement
    if start == 'i':
        print("You get up and enter an abandoned super market...")
        # add a delay
        time.sleep(4)
        # function call for stage 1 logic
        market1()
    #  Opening umbrella user response
    elif start == 'u':
        print("The umbrella opens...")
        time.sleep(8)
    # Incorrect input
    else:
        """rerun the function
        # (recursive statement
        #           - this type of function call typically has a different input than the original)
        """
        Welcome()

# Stage 1 
def market1():
        # user response is inside1
        inside1 = input("You see a dim light in the back left corner \n
                        "and hear a muffled buzz coming from"
                      "the back right. Investigate (L/R): ")

Welcome()


