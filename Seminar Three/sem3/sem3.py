def slide5():

    x = 11

    for i in range(11,16):
        print(i, end=" ")
    print("")

    # range and slicing are very similar, because they have the same arguments
    # 1. start end increment, the index does not include the end
    # 2. range(start, end, increment)
    # 3. string[start:end:increament]
    # 4. -1 cannot be used by range to indicate starting or ending position

    str = "ABCDEFGHIJKLMNOP"    

    for i in str[10:15]: # 10, 11, 12, 13, 14
        print(i, end=" ")
    print("")

    for i in range(5):
        print(str[i], end=" ")
    print("")

    for i in range(0,5):
        print(str[i], end=" ")
    print("")   

    for i in str[0:]:
        print(i, end=" ")
    print("")

    for i in range(0,-1):
        print(str[i], end=" ")
    print("")  

    for i in str[0:None]:
        print(i, end=" ")
    print("")

#slide5()

def slide7():

    for i in range(10, 0, 1):
        print(i, end=" ")
    print("")

    for i in range(10, 2, -2):
        print(i, end=" ")
    print("")

#slide7()

def slide8():

    n = int(input("How many numbers do you have? "))

    if n <= 0:
        print(f"\nThe number {n} is invalid")
    else:
        sum = 0.0
        for i in range(n):
            x = float(input("Enter a number >> "))
            sum = sum + x
            #sum += x
        print(f"\nThe average of the numbers is {sum/n}")

#slide8()

def slide9():

    sum, n, m = 0, 5, 6 # 5 x 6

    #for i in range(0,n):
    for i in range(n):
        sum += m

    print(f"{m} x {n} = {sum}")

#slide9()

def slide10():

    for ch in "Spam!":
        print(ch, end=" ")
    print("")

    str = "Spam!"

    for i in str[0:]:
        print(i, end=" ")
    print("")

#slide10()

def slide13():

    for x in range(11,16):
        print(x, end=" ")
    print("")

    x = 11
    while x < 16:
        print(x, end=" ")
        x += 1
    print("")

#slide13()

def slide14():

    for i in range(11):
        print(i)
    
    i = 0
    while i <= 10:
        print(i)
        i+=1

#slide14()  

def slide16():

    i = 0
    while i <= 5:
        print(i)
        i+=1

    i = 0
    while True:
        if i > 5: break

        if i == 4: 
            i += 1
            continue
        else:
            print(i)
            i+=1

#slide16()

def slide17():

    sum, count= 0.0, 0

    moredata = "yes"

    # while moredata[0]=="y":
    while True:
        if moredata[0]=="n": break
        x = float(input("Enter a number>>"))
        sum += x
        count += 1
        moredata=input("Do you have more numbers (yes or no)?")
    
    print(f"\nThe avearage of the numbers is {sum/count:.2f}")

#slide17()

import random 

def slide23():

    tries = 1
    diceValue=random.randrange(1,6)

    while tries<=3:
        guess = int(input(f"Try {tries}, Enter your guess: "))
        if diceValue == guess:
            print("You got it")
            break
        print("Incorrect")
        tries+=1
    
    if tries > 3:
        print("Your maximun number of tries has been reached")

#slide23()

def slide26():

    for i in range (1, 3):
        for j in 'abc': # loop through j = 'a , 'b', 'c'
            print(i, j)

#slide26()

def slide29():

    playAgain="Yes"

    while playAgain[0].lower()=='y':

        tries = 1

        diceValue=random.randint(1,6)

        maxNumberOfTries = 3

        while tries <= maxNumberOfTries:
            guess = int(input(f"Try {tries}, Enter guess "))
            if guess == diceValue:
                print("You got it")
                break
            print("Incorrect")
            tries+=1
        else:
            print(f"Sorry the value is {diceValue}")
        
        playAgain = input("Continue? (Y/N) ")

    print("End of the Game")

slide29()
