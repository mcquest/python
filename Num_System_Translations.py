#mcquest
#input one number system to output another
"""
TODO:
 - Add comments
 - Make more user friendly (list options, ask to enter another number)
"""

b =  input("Enter a binary number: ")

def Base2to10(num0):
    lnum = []
    for b in num0:
      # To note: Strings can also be sequenced as lists 
      binl += [b]
    # store variable for length of binary number
    j = 0
    # holder variable for decimal value
    t = 0
    l = len(b)-1
    while j <= l:
        if binl[l-j] == "1":
            t = t + (2 ** j)
        j +=1
        
    print(t)

Base2to10(b)

def Base10to2Builtin():
    i = input("Enter an integer: ")
    print(bin(int(i)))

#Base10to2Builtin()

def Base10to2A():
    ii = input("Enter an integer: ")
    i = int(ii)
    exp = 0
    num0 = []
    expCheck = 0
    while i > 2**exp:
         exp +=1
    lexp = exp - 1
    num0 = ["0"]*exp
    #num0[expCheck] = "1"
    while expCheck < exp:
        if i >= 2**lexp:
            num0[expCheck] = "1"
            expCheck+=1
            i = i - (2**lexp)
            lexp -= 1
        else:
            expCheck+=1
            lexp -= 1
    print(''.join(num0))

#Base10to2A()


"""
With mod(remainder) % and division
"""
def Base10to2B():
    i = input("Enter an integer: ")
    if(int(i) <= 1):
        print(i)
    binaryValue = ''
    remainder = int(i)
    while remainder > 0:
        binaryValue = str(remainder % 2) + binaryValue
        remainder = remainder // 2    
    print(binaryValue)

Base10to2B()
