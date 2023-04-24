"""
Header Comment
Example Text Adventure..
Script Name: TextAdventure.py
Coder Name: Charles 
What happens when the script is run?:
User is given a series of choices and must make decisions
to discover and adapt to their environment

TODO
+ Add 3-5 minutes of user experience
+ Add comments to every line
"""

# Import time and system 
# classes/libraries to use built in functions from it 
import sys 
import time

# Empty list
e = []

# Map list... 1 represents the player
# mp[0] = 0, mp[3] = 1
mp = [0,0,0,1,0,0,0,0]

#List of potential yes answers 
ys = ["yes", "Yes", "absolutely"]

choices = ["Choices -> "]

#empty print to create space
print()


# Function to store Introductory decisions
def Welcome():
    global choices
    s = ""
    for y in ys:
        s = s+y+".\n"
    Print_scroll("Welceome to an adventure through text...\n"
          "Type one of the following then enter to answer yes:\n" + s)
    
    # Opening Line print statement & user input holder variable
    start = input("\n You are sitting outside on a bench and it starts to"
                " rain, \n do you want to use your umbrella or go inside? (Type: u or i) : ")
    choices += start
    # Check user response to start with if statement
    if start == 'i':
        Print_scroll("You get up and enter an abandoned super market...")
        # add a delay
        print (choices)
        time.sleep(2)
        # function call for stage 1 logic
        Market1()

    #  Opening umbrella user response statement
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

# Stage 1 function definition
def Market1():
        global choices
        # user response is inside1 variable
        inside1 = input("You see a dim light in the back left corner \n"
                        "and hear a muffled buzz coming from"
                      "the back right. Investigate (left or right): ")
        choices+=inside1
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

# Import time and system 
# classes/libraries to use built in functions from it 
import sys 
import time
    
#Defining word scroll function with a parameter (characters print out one at a time)
def Print_scroll(phrase):
    if len(phrase) > 28:
        #for every character in the output string
        for char in phrase:
            #print characters one at a time 
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.02) #seconds
    else:
        print(phrase)
Welcome()


