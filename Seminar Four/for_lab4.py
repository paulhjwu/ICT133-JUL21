import math
from random import randint

def Q6d():

    def inputSwimmers():

        swimmers = []
        for i in range(5):
            name = input(f"Enter lane {i+1} swimmer: ")
            swimmers.append(name)

        return swimmers

    def inputTiming(swimmers):

        timings = []
        for i in swimmers:
            aTime = float(input(f"Enter timing for {i}: "))
            timings.append(aTime)

        return timings

    def printResults(x):

        for elem in x:
            print(f"{elem[0]:<8s}{elem[1]:>10.2f}s")

    def keyFunc(elem):
        return elem[1]

    swimmers = inputSwimmers()
    timings = inputTiming(swimmers)

    x = list(zip(swimmers, timings))

    x.sort(key=keyFunc)

    printResults(x)

Q6d()

def Q6():

    def inputSwimmers():

        swimmers = []
        for i in range(5):
            name = input(f"Enter lane {i+1} swimmer: ")
            swimmers.append(name)

        return swimmers

    def inputTiming(swimmers):

        timings = []
        for i in swimmers:
            aTime = float(input(f"Enter timing for {i}: "))
            timings.append(aTime)

        return timings

    def printResults(swimmers, timings):

        #name = "Name"
        #time = "Time"
        #print(f"{name:<8s}{time:<10s}")
        for i, item in enumerate(swimmers):
            print(f"{item:<8s}{timings[i]:>10.2f}s")
        print(f"Fastest is {min(timings):>5.2f}s")

    swimmers = inputSwimmers()
    timings = inputTiming(swimmers)

    printResults(swimmers, timings)

#Q6()

def Q5():

    answer = ( 'a', 'b', 'b', 'a', 'd', 'c', 'b', 'a', 'b', 'c')
    theInput = [0, ] * 10

    for i in range(10):
        theInput[i] = input(f"Q{i+1}: ")

    count = 0

    for i in range(10):
        
        if theInput[i]==answer[i]:
            count+=1
            msg= "correct"    
        else:
            msg = f"incorrect, answer is {answer[i]}" 
        
        print(f"Q{i+1}: {theInput[i]} {msg}")
    
    print(f"Total {count} out of 10 correct")

#Q5()

def Q4():
    
    nric = input(f"NRIC No.(with official reference) = ")

    checkStr = "ABCDEFGHIZJ"
    weight = (2, 7, 6, 5, 4, 3, 2)

    sum = 0
    index = 0
    for i in nric[1:len(nric)-1]:
        if i[0].isdigit():
            sum += (int(i)*weight[index]) # ascii 0 is 48
            index += 1

    remainder = sum % 11
    checkDigit = 11 - remainder 

    if nric[len(nric)-1] != checkStr[checkDigit-1]:
        print(f"The Reference Character is not correct")
    else:
        print(f"The Reference Character is correct")

#Q4()

def Q3():

    diceCount = [0, 0, 0, 0, 0, 0, 0]

    for i in range(100):   
        diceValue = randint(1, 6)
        diceCount[diceValue]+=1
    
    print(f"Dice  Occurrence")

    for i in range(len(diceCount)-1):
        print(f"{i+1:<6d}{diceCount[i+1]:<6d}")

#Q3()

def Q2b():

    infile = open("customer.dat", 'r')
    outfile = open("bmi.dat", 'w')

    str1 = "Name"
    str2 = "Weight"
    str3 = "Height"
    str4 = "BMI"

    print(f"{str1:<8s}{str2:<8s}{str3:<8s}{str4:<8s}", file=outfile)

    for line in infile:
        name, weight, height = line.split(',')
        weight = float(weight)
        height = float(height)

        bmi = weight / pow(height, 2)

        print(f"{name:<8s}{weight:<8.2f}{height:<8.2f}{bmi:<8.2f}", file=outfile)

    infile.close()
    outfile.close()

#Q2b()

def Q2a():

    infile = open("customer.dat", 'r')

    str1 = "Name"
    str2 = "Weight"
    str3 = "Height"
    str4 = "BMI"

    print(f"{str1:<8s}{str2:<8s}{str3:<8s}{str4:<8s}")

    for line in infile:
        name, weight, height = line.split(',')
        weight = float(weight)
        height = float(height)

        bmi = weight / pow(height, 2)

        print(f"{name:<8s}{weight:<8.2f}{height:<8.2f}{bmi:<8.2f}")
    
    infile.close()

#Q2a()

def Q1():

    infile = open("rainfall.dat", 'r')
    days = 0
    noRainDays = 0
    totalRain = 0
    dailyRain = []

    for line in infile:
        rainDaily = float(line)
        dailyRain.append(rainDaily)
        if rainDaily == 0.0:
            noRainDays += 1
        else:
            totalRain += rainDaily
        days += 1

    print(f"Rainfall Summary")
    print(f"Average rainfall {totalRain/days:5.2f}mm")
    print(f"No of days with no rain {noRainDays} days")
    print(f"Highest rainfall recorded {max(dailyRain):5.2f}mm")
    infile.close()

#Q1()