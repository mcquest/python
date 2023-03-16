#mcquest
#input one number system to output another
"""
TODO:
 - Add comments
 - Make more user friendly (list options, ask to enter another number)
"""
def Base2to10():
    b =  input("Enter a binary number: ")
    j = 0
    t = 0
    l = len(b)-1
    while j <= l:
        if b[l-j] == "1":
            t = t + int(b[l-j]) * (2 ** j)
        j +=1
        
    print(t)

#Base2to10()

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
