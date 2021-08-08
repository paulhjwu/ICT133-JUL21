
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

