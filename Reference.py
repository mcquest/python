"""
MCQuest
Python Reference Script

    '\':  next line 
    '\n': new line
    '\t': tab

5 Main Coding Structures:
Comment
Statement
Variable
Loop
Function
"""

import sys
from time import sleep
import random

#Comment """"""
#Statement -> Every line of code is a statement
print(False and True) #-> False
#Variables
x = 1
s = "pi \
za"
#print(x)

#Function
def fun():
    return

#Defining word scroll function (characters type out one at a time)
def print_scroll(output):
    #For loop (for every character in the output)
    for char in output:
        #print characters one at a time - not using new line every time
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(.02)
        #sleep to create slight pause between character scroll

    #empty print to create new line after statement
    print()

"""
.lower(): string -> lowercase
.upper()
"""  

#Global list -- value changed later in code
l1 = [2,1,4]

#Loops: while & for
for item in reversed(l1):
    break
    #print(item)
    

#Initialization variable
i = 0
while i < 5:
    #print (i)
    i = i + 1
    i+=1

list2 = []
for x in [3,2,1]:
    list2 += [x] 
print(list2)


#global v7
v7 = 100
def funExample():
    l1 = 1
    #print (v7)
#global l1
l1 = 8

funExample()

#check to see if main script otherwise don't run if imported
if __name__ == '__main__':
    # run main()
    pass

"""
Truth tables
"""





