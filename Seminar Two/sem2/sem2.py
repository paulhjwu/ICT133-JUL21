from typing import get_args


def slide3():

    a = 'aaa'
    b = "aaa"
    c = '''aaa'''

    print(a==b)
    print(b==c)
    print(c==a)

#slide3()

def slide4():

    a = "Hello Bob"

    print(a[0])
    print(a[-1])

    # looping

    y = len(a)
    for i in range(len(a)): # for i in range(9):
        print(a[i], end="")
    print("")
    
    for i in range(-1,-10,-1):
        print(a[i], end="")
    print("")
    
    for i in range(-9,0):
        print(a[i], end="")
    print("")

#slide4()

def slide5():

    greet="Hello Bob"
    print(greet[-3])

#slide5()

def slide7_8():

    greet = "Hello Bob"
    print(greet[0:3])
    print(greet[3:0:-1])
    print(greet[:5])
    print(greet[5:])
    print(greet[:])
    print(greet[::-1])

    print(greet[0:2]*3)

#slide7_8()

def slide11():

    firstName, lastName = input("Enter first name followed by last name: ").split()
    print(firstName)
    print(lastName)

    # int(input(" Enter a number "))

    coords = input("Enter the point coordinates (x,y): ").split(",")
    x,y = float(coords[0]), float(coords[1])
    print(x)
    print(y)

#slide11()

def slide17():

    x = "centered: {0:^5} {1}".format("Hi!", "there")
    print(x)

    y = "Hi!"
    z = "there"
    print(f"centered: {y:^5} {z}")

    aList = ["Hi!", "there"]
    print(f"centered: {aList[0]:^5} {aList[1]}")

#slide17()

def slide30():

    print("A" > "a")
    print("A" < "A1")

#slide30()

def TMA_related():

    # XOR 1 XOR 0 = 1, 
    a=1
    b=0
    print(a and b)
    print(a or b)
    print(not a)
    print(not b)
    print(not a or b)

#TMA_related()

def slide42():

    num = int(input("Enter a number "))

    sign = "+ve" if num >= 0 else "-ve"
    evenOrOdd = "even" if num%2==0 else "odd"
    print(sign, evenOrOdd)

#slide42()

def slide44():

    gender = input("Enter gener (M/n) ")

    if gender in "mM":
        print(gender)

slide44()