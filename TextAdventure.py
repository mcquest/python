"""
Header Comment
Example Text Adventure..
Script Name: TextAdventure.py
Coder Name: Charles 
What happens when the script is run?:
User is given a series of choices and must make decisions
to discover and adapt to their environment
"""

# Import time and system 
# classes/libraries to use built in functions from it 
import sys 
import time

#List of potential yes answers 
ys = ["yes","Yes","y","okay","sure","...","..","."]
choices = ["Choices -> "]

#empty print to create space
print()

#Defining word scroll function (characters print out one at a time)
def print_scroll(o):
    #for loop checking every character in the output string
    for c in o:
        #print characters one at a time 
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.02) #seconds

# Introductory decisions
def Welcome():
    global choices
    s = ""
    for y in ys:
        s = s+y+".\n"
    print("Welceome to an adventure through text...\n"
          "Type one of the following then enter to answer yes:\n" + s)
    
    # Opening Line
    start = input("\n You are sitting outside on a bench and it starts to"
                " rain, \n do you want to use your umbrella or go inside? (Type: u or i) : ")
    choices += start
    # Check user response to start with if statement
    if start == 'i':
        print("You get up and enter an abandoned super market...")
        # add a delay
        print (choices)
        time.sleep(2)
        # function call for stage 1 logic
        Market1()

    #  Opening umbrella user response
    elif start == 'u':
        print("The umbrella opens...")
        print (choices)
        time.sleep(1)
        Umbrella1()
    # Incorrect input
    else:
        """rerun the function
        # (recursive statement
        #           - this type of function call typically has a different input than the original)
        """
        Welcome()

# Stage 1 
def Market1():
        # user response is inside1
        inside1 = input("You see a dim light in the back left corner \n"
                        "and hear a muffled buzz coming from"
                      "the back right. Investigate (left or right): ")
        if input == "left":
            Left0()
            
        if input == "right":
            Right0()

def Umbrella1():
    umbrain1 = input("\n Your umbrella opens preventing you from getting wet.\n"
                     "Would you like to stand up? \n\n")

def Left0():
    print("You have gone left...")
    
def Right0():
    print()

Welcome()


