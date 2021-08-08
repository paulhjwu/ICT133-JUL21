### The following was covered during the Virtual lab

import math

def Q5():

    data=float(input("Amount of data used(GB):"))
    if (data<2):
        print("Charge is $5.00")
    else:
        extra_data=data-2
        extra_cost=math.ceil(extra_data/0.1)
        total_cost=extra_cost+5
        print(f"Charge is ${total_cost:.2f}")

#Q5()

def q5():


    import math
    data = float(input("Amount of data used (GB): "))
    if data <= 2 :
        print ("Charge is $5.00")
    else:
        extra_data = data - 2
        extra_data = round(extra_data, 4)
        extra_charge = math.ceil(extra_data * 10)
        total_cost = 5 + extra_charge
        print (f'Charge is ${total_cost:.2f}')
#q5() 

def Q6():

    a=int(input("Enter integer A: "))
    b=int(input("Enter Integer B: "))

    # a is even or not 
    cond1 = True if a % 2 == 0 else False
    # b is even or not
    cond2 = True if b % 2 == 0 else False

    if cond1 and cond2:
        print("Both are even")
    elif (not cond1) and (not cond2):
        print("Both are odd")
    else:
        print("One is odd, and the other is even")

Q6()

def Q7():
    
    nric = input("Enter NRIC ")

    if len(nric) != 9:
        print(f"Length must be exactly 9 characters")
    elif nric[0].upper() not in "STFG":
        print(f"The first letter must be S, T, F, or G ")
    elif not nric[1:8].isdigit():
        print(f"Must consist of 7 digits")
    elif not nric[-1].isalpha():
        print(f"The reference letter must be an alphabet")
    else:
        print("Nric is valid")

Q7()

##### The following was not covered during the virtual lab

import math
from math import ceil

def Q11():

    amount = float(input("Enter Amount: "))
    if amount < 1000:
        print("No install, pay full amount")
    else:
        plan=int(input("Pay in 0, 6, or 12 month installment: "))
        if plan == 0:
            print(f"Please pay ${amount:.2f}")
        elif plan == 6:
            pay = (amount * 1.05) / 6
            print(f"{plan} month installment plan of ${pay:.2f}")
        elif plan == 12:
            pay = (amount * 1.1) / 12
            print(f"{plan} month installment plan of ${pay:.2f}")
        else:
            print(f"Invalid installment plan")
#Q11()

def Q10():

    a = int(input('Enter side a: '))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))

    if a+b<=c or a+c<=b or b+c<=a:
        print("Invalid sides")
    elif a==b and b==c:
        print("Equilateral")
    elif a==b or b==c or c==a:
        print("Isosceles")
    else:
        print("scalene")

    print("End of q10()")

#Q10()

def Q9():

    a = input("Kindly enter arithmetic experssion: ")
    l = len(a)

    # 1.23*3.45 

    P = a.find("+")
    M = a.find("-")
    T = a.find("*")
    D = a.find("/")

    L = max(P, M, T, D)

    n1 = float(a[0:L])
    n2 = float(a[L+1:])

    if P > 0:
        print(f"Result: {n1+n2:6.2f}")
    elif M > 0:
        print(f"Result: {n1-n2:6.2f}")
    elif T > 0:
        print(f"Result: {n1*n2:6.2f}")
    elif D > 0:
        print(f"Result: {n1/n2:6.2f}")
    else:
        print("Error!")

#Q9()

def Q8():

    dataUsed = float(input("Amount of data used (GB): "))

    charge = 5

    if dataUsed <= 0:
        print("Nto Valid Usage")
    elif dataUsed <= 2:
        pass
    elif dataUsed <= 4: 
        surplus = dataUsed - 2
        charge += ceil(surplus * 10)
    else:
        charge = 25
    
    print(f"Charge is $ {charge:6.2f}")

    return print("End of Q8")

#Q8()

def Q4():

    theString = input("Enter the string ")

    theReverse = theString[-1::-1]

    if theString == theReverse:
        print(f"The string {theString} is a palindrome")
    else:
        print(f"The string {theString} is not a palindrome")

#Q4()

def Q3():

    firstN, secondN = input("Enter two numbers: ").split()

    firstN = int(firstN)
    secondN = int(secondN)

    if firstN == secondN:
        print(f"The two numbers are equal")
    else:
        print(f"The two numbers are not equal")

#Q3()

def Q2():

    firstP, secondP = input('Enter strings: ').split()

    firstP = firstP[-1::-1]
    secondP = secondP[-1::-1]

    print(f"Output: {firstP} {secondP}")

#Q2()

def Q1():

    # "joe@suss.edu.sg"  [start:end:incre]

    email = input('Enter email: ')
    index = email.find('@')

    if index == -1:
        print("Invalid email")
    else:
        name = email[:index]
        org = email[index+1:]
        print(f'Name is {name}')
        print(f'Organization is {org}')

#Q1()