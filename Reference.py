"""
MCQuest
Python Reference Script

What is a reference script?
    + Write key statements-phrases
    + Write main coding structures
    + Store useful functions to move between projects
    
    
    

    '\':  next line 
    '\n': new line
    '\t': tab

5 Main Coding Structures:
Comment
Statement
Variable
Loop
Function


(" ~~~~~~ "
" ~~~~~~~ "
" ~~~~~~~ ")


"""

import time
import random
import sys

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
    time.sleep(5)
    return


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
    global v7
    print (v7)
#global l1
l1 = 8

funExample()

#check to see if main script otherwise don't run if imported
if __name__ == '__main__':
    # run main()
    pass

#Defining word scroll function (characters print out one at a time)
def print_scroll(output):
    #for every character in the output string
    for char in output:
        #print characters one at a time 
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(.02) #seconds

# Inspired by J C        
# Define a function to convert a number from one base to another
def base_conversion(number, from_base, to_base):
    # First, convert the number to base 10
    base_10_num = 0
    for i in range(len(number)):
        digit = int(number[i], from_base)
        power = len(number) - 1 - i
        base_10_num += digit * (from_base ** power)
    
    # Next, convert the base 10 number to the target base
    result = ""
    while base_10_num > 0:
        digit = base_10_num % to_base
        result = str(digit) + result
        base_10_num //= to_base
    
    return result

# Define a function to prompt the user for input and output bases and perform the conversion
def translate_number():
    # Prompt the user for the input number and its base
    number = input("Enter the number to convert: ")
    from_base = int(input("Enter the base of the input number: "))
    
    # Prompt the user for the output base
    to_base = int(input("Enter the base of the output number: "))
    
    # Convert the number to the output base
    result = base_conversion(number, from_base, to_base)
    
    # Print the result
    print("The converted number is:", result)

# Call the translate_number() function to start the program
translate_number()



"""
TODO
Truth tables
"""





