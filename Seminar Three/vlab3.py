import math

def Q11():

    def divide(x, y):
        quotient = 0
        remainder = x - y
        while remainder >= 0:
            quotient += 1
            remainder -= y
        return quotient, (y + remainder)

    def main():
        x, y = (int(i) for i in input("Enter two numbers: ").split())
        q, r = divide(x,y)
        print(f"The input is {x} and {y}, the quotient is {q}, and the remainder is {r} ")

    main()

Q11()

def Q10():

    def getValidValue(msg, x, y):
        mark = int(input(msg))
        if x <= mark <= y:
            return mark
        else:
            print(f"Invalid input, Try again")
            return 0
    
    def main():
        mark = getValidValue("Enter Mark ", 1, 100)
        while True:
            if mark != 0:
                print(f"The mark entered is {mark}")
                break
            else:
                mark = getValidValue("Enter Mark ", 1, 100)
    
    main()

#Q10()

def Q9():

    def  sumSquares(num):
        sum = 0
        for i in range(num):
            sum += math.pow(i+1, 2)
        return sum
    
    def main():

        num = int(input(f"Enter the number: "))
        print(f"The sum of squares of {num} is {sumSquares(num)}")

    main()

#Q9()

def Q8():

    def displayFromTo(x, y): # was Q1a()

       for i in range(x, y+1):
            print(f"{i}")

    def main():
        fNum = int(input("Enter first number: "))
        sNum = int(input("Enter second number: "))
        displayFromTo(fNum, sNum)

    main()

#Q8()  

from random import choice, randint

def Q7b():

 
    on = 'y'



    while on == 'y':

        answer = randint(1, 100)
        tries = 0
        guess=int(input(f"Enter your guess: "))
        
        while True:
            tries+=1
            if 1 <= guess <= 100:
                if guess==answer:
                    print(f"You got it in {tries} tries")
                    break
                else:
                    if guess > answer:
                        print(f"Too high")
                    else:
                        print(f"Too low")
            else:
                print(f"outside limit.")

            guess=int(input(f"Enter your guess: "))
        
        on = input("Continue game? (y/n): ")

#Q7b()


def Q7a():

    guess=int(input(f"Enter your guess: "))

    answer = randint(1, 100)
    tries = 0

    while True:
        tries+=1
        if 1 <= guess <= 100:
            if guess==answer:
                print(f"You got it in {tries} tries")
                break
            else:
                if guess > answer:
                    print(f"Too high")
                else:
                    print(f"Too low")
        else:
            print(f"outside limit.")

        guess=int(input(f"Enter your guess: "))

#Q7a()

def Q6d():

    def Q6a_1():

        guess = input("Head or Tail (H or T): ").upper()
        answer = choice(("H", "T"))
        if (guess[0] not in "HT") or (guess[0] != answer):
            print("Incorrect!")     
            return 0   
        else:
            print("Correct!")
            return 1
    
    yes = input("Do you want to play again? (y/n) ")
    while yes == "y":
        count = 1
        while True:
            if Q6a_1() == 0: 
                count += 1
            else:
                break
        print(f"You got it in {count} tosses!")
        yes = input("Do you want to play again? (y/n) ")

#Q6d()

def Q6c():

    def Q6a_1():

        guess = input("Head or Tail (H or T): ").upper()
        answer = choice(("H", "T"))
        if (guess[0] not in "HT") or (guess[0] != answer):
            print("Incorrect!")     
            return 0   
        else:
            print("Correct!")
            return 1

    count = 1
    while True:
        if Q6a_1() == 0: 
            count += 1
        else:
            break
    print(f"You got it in {count} tosses!")
        
#Q6c()

def Q6b():

    def Q6a_1():

        guess = input("Head or Tail (H or T): ").upper()
        answer = choice(("H", "T"))
        if (guess[0] not in "HT") or (guess[0] != answer):
            print("Incorrect!")     
            return 0   
        else:
            print("Correct!")
            return 1

    rounds = int(input("How many rounds to play? : "))

    yes = 0
    for i in range(rounds):
        yes += Q6a_1()

    print(f"You guess {yes} correct out of {rounds} rounds")

#Q6b()

def Q6a():


    guess = input("Head or Tail (H or T): ").upper()

    answer = choice(("H", "T"))

    if (guess[0] not in "HT") or (guess[0] != answer):
        print("Incorrect!")        
    else:
        print("Correct!")

#Q6a()

def Q5():

    def menu():
        return int(input('''
    Menu
    1. Option 1
    2. Option 2
    3. Option 3
    0. Quit 
    Enter choice: '''))

    def main():
        choice = menu()
        while choice != 0:
            print(f"    Option {choice} selected")
            choice = menu()
    
    main()

#Q5()

def Q4():

    total = 0
    quant = int(input("Enter quantity: "))

    while True:
        if quant == -1: break
        price = float(input("Enter unit price: "))
        subtotal = quant * price
        print(f"Subtotal is ${subtotal}")
        total += subtotal
        quant = int(input("Enter quantity: "))

    print(f"Total price is ${total:<5.2f}")
    print(f"GST is ${total*0.07:<5.2f}")
    print(f"Plesae pay ${total*1.07:<5.2f}")

#Q4()

def Q3c():
    num = int(input("Enter number: "))
    while num != -1:
        if 2 <= num <= 10:
            for i in range(num):
                print(f"{i+1} x {num} = {(i+1)*num}")
        else:
            print(f"Invalid. Enter again")

        num = int(input("Enter number: "))

#Q3c()

def Q3b():
    num = int(input("Enter number: "))
    while num != -1:
        for i in range(num):
            print(f"{i+1} x {num} = {(i+1)*num}")
        num = int(input("Enter number: "))

#Q3b()

def Q3a():

    num = int(input("Enter number: "))

    for i in range(num):
        print(f"{i+1} x {num} = {(i+1)*num}")

#Q3a()

def Q2c():

    inputStr = input("Input string: ")
    while True:     
        if inputStr == 'exit': break 
        repeat = int(input("Number of times to repeat: "))       
        for i in range(repeat):
            print(f"{inputStr}")      
        inputStr = input("Input string: ")

#Q2c()

def Q2b():

    inputStr = input("Input string: ")

    for i in range(len(inputStr)):
        print(f"{inputStr[:i+1]}")

#Q2b()

def Q2a():

    inputStr = input("Input string: ")
    num = int(input("Number of times to repeat: "))

    for i in range(num):
        print(f"{inputStr}")

#Q2a()

def Q1c():

    fNum = int(input("Enter first number: "))
    sNum = int(input("Enter second number: "))

    if fNum < sNum:
        begin = fNum
        end = sNum+1
        increment = 1
    else:
        begin = fNum
        end = sNum - 1
        increment = -1

    for i in range(begin, end, increment):
        print(f"{i}")

#Q1c()

def Q1b():

    fNum = int(input("Enter first number: "))
    sNum = int(input("Enter second number: "))

    sum = 0
    for i in range(fNum, sNum+1):
        print(f"{i}")
        sum += i

    print(f"The sum is {sum}")

#Q1b() 

def Q1a():

    fNum = int(input("Enter first number: "))
    sNum = int(input("Enter second number: "))

    for i in range(fNum, sNum+1):
        print(f"{i}")

#Q1a()        
