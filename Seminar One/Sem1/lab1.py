### The first part is done after the Vlab

def q8():

    loan = float(input("Enter the loan amount: "))
    duration = int(input("Enter the duration (in years): "))
    interest = float(input("Enter the interest rate: "))

    c = loan * pow(( 1 + interest/100), duration)

    print(f"The total compound interest to be paid is {c:10.2f}")

#q8()

def q7():

    #input
    s1 = float(input('Enter side a: '))
    s2 = float(input('Enter side b: '))
    s3 = float(input('Enter side c: '))

    s4 = 1/2 * (s1 + s2 + s3)

    area = math.sqrt(s4 * (s4 - s1) * (s4 - s2) * (s4 - s3) )
    area = sqrt(s4 * (s4 - s1) * (s4 - s2) * (s4 - s3) )

    print(f'The area is {area}')

#q7()

def q6():

    # input
    bill = float(input('Enter meal amount ($):'))

    cost = bill * 0.5
    service = cost * 0.1
    GST = (cost + service) * 0.07
    total = cost + service + GST

    print(f'Receipt')
    print(f'Cost of meal:   ${bill:6.2f}')
    print(f'50% discount:   ${cost:6.2f}')
    print(f'Service charge: ${service:6.2f}')
    print(f'GST:            ${GST:6.2f}')
    print(f'Total amount:   ${total:6.2f}')

#q6()

def q2():

    n1 = float(input('Enter the first number : '))
    n2 = float(input('Enter the second number : '))
    n3 = float(input('Enter the third number : '))

    sum1 = n1 + n2 + n3
    ave1 = sum1/3

    print(f"The sum of the 3 numbers is {sum1}, and the average is {ave1}")

#q2()

#### Below have been done during the session

def Q5():

    # input
    cents = int(input("Enter the number of cents "))

    c50 = cents // 50
    c10 = (cents % 50) // 10
    c5 = (cents % 10) // 5
    c1 = cents % 5

    print(f'{cents} cents is equal to {c50} 50-cents, {c10} 10-cents, {c5} 5-cents, {c1} cents')

#Q5()

def Q9():

    hrs = int(input("Enter the current hr: "))
    mins = int(input("Enter the current min: "))
    secs = int(input("Enter the current sec: "))

    # calculating the new time after 1 sec
    secs_new = (secs + 1) % 60
    mins_new = (((secs + 1) // 60) + mins) % 60
    hrs_new = (((((secs + 1) // 60) + mins) // 60) + hrs ) % 24

    print(f"Curren clock time is {hrs}:{mins}:{secs}")
    print(f"After 1 sec, the clock time is {hrs_new:02d}:{mins_new:02d}:{secs_new:02d}")

    f = 92.0123

    print(f"The floating point nubmer has 7 digits, 3 decimal points: {f:07.3f}")

#Q9()

def Q4():

    num = int(input("Enter the number in terms of seconds: "))

    # Hr:Mn:Sc = 24:60:60
    h = num // 3600
    m = num // 60 % 60
    s = num % 60

    print(f'{num} seconds is equal to {h} hours, {m} minutes, and {s} seconds') 
    # f'   '   
    # f"   "     
#Q4()

def Q1():

    f = float(input('Enter the temperature in Fahrenheit: '))

    c = 5 / 9 * ( f - 32 )

    print("The following temperature is", c, "degree centigrade")

#Q1()

def Q3():

    # numberinput = int(input("Enter 3 digits here: "))
 

    # #formula of sum of digits
    # hundredth_digit = numberinput // 100
 
    # tens = numberinput % 100
    # tenth_digit = tens // 10

    # ones_digit = tens % 10


    # print ("Sum of numbers", hundredth_digit + tenth_digit + ones_digit)
    # print ("Product of numbers", hundredth_digit * tenth_digit * ones_digit)


    num3 = input("Enter 3 digits here: ")
    a, b, c = int(num3[:1]), int(num3[1:2]), int(num3[-1:])

    a, b, c = int(num3[0]), int(num3[1]), int(num3[2])

    print ("Sum of numbers", a + b + c)
    print ("Product of numbers", a * b * c)

#Q3()