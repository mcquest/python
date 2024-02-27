"""
Example Text Adventure..
Script Name: TextAdventure.py
Coder Name: Charles 
What happens when the script is run?:
User is given a series of choices and must make decisions
to discover and adapt to their environment
"""

inventory = []
belt = []
backpack = []
cart = []
shippingcratecontents = [] 
basket = []

people = []
places = []
positivechoices = []
negativechoices = []
choices = []



# Import time class file to use functions in it 
import time
# Global Variable // When less than 0, the game becomes off balance 
balance = 20

def DotDelay(p):
    for number in range(p):
        print("."*p)
        time.sleep(1)
    



# function to run introductory decisions
def WelcomeStatements1():
    global balance
    # Statement to store variable Opening question Line
    start1 = input("You are sitting outside on a bench and it starts to "
                   "rain, \n do you want to use your yellow umbrella or go inside? (u/i) : ")
    print(start1.__len__())
    # Check user response to start with if statement
    if start1 == 'i':
        print("You get up and enter an abandoned super market...")

        balance = balance - 5
        print("Your balance has decreased and is now", balance)
        
        # Statement to add a delay with sleep function 
        time.sleep(4)
        # function call for stage 1 logic
        Market1()
        
    #  Opening umbrella user response
    elif start1 == 'u':
        
        balance = balance + 7000
        print("Your ability to balance has increased and is now", balance)
        
        print("The umbrella opens...")
        time.sleep(4)
        print(".......")
        time.sleep(8)
        Umbrella1()
        
    # Incorrect input
    else:
        # rerun the function
        WelcomeStatements1()


# Stage 1 
def Market1():
        # user response is inside1
        inside1 = input("You see a dim light in the back left corner \n"
                        "and hear a muffled buzz coming from"
                      "the back right. Investigate (L/R): ")
        

def Umbrella1():
    print("****You open the umbrella and confetti comes out!!****")
    u1 = input("You see a group of people with black umbrellas and one red... Do you join them? (Y/N) ")
    if u1 == "Y":
        Spaghetti()
    if u1 == "N":
        UptheSt()
    else:
        Umbrella1()

 # function to store spaghetti options   
def Spaghetti():
    
    # Print statement to display text to screen 
    print("You have been offered spaghetti")
    
    # variable to store user input
    s1 = input(" Do you accept? (Yes or No) ")

    # if statement to check what the user has typed in
    if s1 == "Yes":
        print()

    # elif or else if statement to check other user input
    elif s1 == "No":
        print()

def UptheSt():
    print("You continue up the street from the park bench you were sitting on"
          "\n you turn right down the next street to see a field of grass with moose in"
          "\n the distance.")
    i4 = input("Approach the moose? (approach) or Get a vantage point from the building"
               "next to you? (vantage)" )

if __name__ == '__main__':
    DotDelay(1)
    DotDelay(2)
    WelcomeStatements1()


