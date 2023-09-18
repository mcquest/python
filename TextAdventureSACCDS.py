"""
Example Text Adventure..
Script Name: TextAdventure.py
Coder Name: Charles 
What happens when the script is run?:
User is given a series of choices and must make decisions
to discover and adapt to their environment
"""


# Import time class file to use functions in it 
import time



# function to run introductory decisions
def Welcome1():
    # Statement to store variable Opening question Line
    start = input("You are sitting outside on a bench and it starts to"
                " rain, \n do you want to use your yellow umbrella or go inside? (u/i) : ")
    # Check user response to start with if statement
    if start == 'i':
        print("You get up and enter an abandoned super market...")
        # Statement to add a delay with sleep function 
        time.sleep(4)
        # function call for stage 1 logic
        Market1()
    #  Opening umbrella user response
    elif start == 'u':
        print("The umbrella opens...")
        time.sleep(4)
        print(".......")
        time.sleep(8)
        Umbrella1()
    # Incorrect input
    else:
        # rerun the function
        Welcome1()

# Stage 1 
def Market1():
        # user response is inside1
        inside1 = input("You see a dim light in the back left corner \n"
                        "and hear a muffled buzz coming from"
                      "the back right. Investigate (L/R): ")

def Umbrella1():
    print("You open the umbrella and confetti comes out!!****")
    u1 = input("You see a group of people with black umbrellas and one red... Do you join them? (Y/N) ")
    if u1 == "Y":
        Spaghetti
    
    

#def Umbrella1():
        

Welcome1()


