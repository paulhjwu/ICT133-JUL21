### Below is covered during Virtual Lab 
### Scroll to the end to find Q4 and Q5 which are not covered

# import random
from random import randint, randrange

def Q6():

    def recordSwimmers():

        swimmers = []

        for i in range(5):
            name = input(f"Enter lane {i+1} swimmer: ")
            swimmers.append(name)

        return swimmers

    def recordTiming(swimmers):

        timings = []

        for i in range(5):
            aTime = float(input(f"Enter the timing of {swimmers[i]} "))
            timings.append(aTime)

        return timings
    
    def printResults(swimmers, timings):

        for i in range(5):
            print(f"Swimmer {swimmers[i]}'s time is {timings[i]}")
    
    def printResultsOneList(oneList):

        for i in range(5):
            print(f"Swimmer {oneList[i][0]}'s timing is {oneList[i][1]}")

    swimmers = recordSwimmers()
    #print(swimmers)
    timings = recordTiming(swimmers)
    #print(timing)

    def keyFunc(elem):
        return(elem[1])

    x = list(zip(swimmers, timings))
    x.sort(reverse=True, key=keyFunc)

    printResults(swimmers, timings)
    printResultsOneList(x)

Q6()

def Q3():

    diceCount=[0,]*7

    for i in range(100):
        # diceValue=random.randint(1,6)
        diceValue=randint(1,6)
        diceCount[diceValue]+=1

    print(f"Dice Occcurence")

    total_num = 0
    for i in range(len(diceCount)-1):
        print(f"{i+1:<5d}{diceCount[i+1]:<5d}") # >: right justified
        total_num += diceCount[i+1]
  
    print(f"Total {total_num}")

#Q3()

def Q2a():

    infile = open("customer.dat", 'r')

    str1 = "Name"
    str2 = "Weight"
    str3 = "Height"
    str4 = "BMI"

    print(f"{str1:8s}{str2:8s}{str3:8s}{str4:8s}")

    for line in infile:
        name, weight, height = line.split(',')

        weight = float(weight)
        height = float(height)

        bmi = weight / pow(height, 2)

        print(f"{name:8s}{weight:<8.2f}{height:<8.2f}{bmi:<8.2f}")

#()

# Name
# John
# Peter
# ...
# Joe
# Weight Height BMI
# 50
# 1.4
# 25.51
# 60
# 1.7
# 20.76
# 45
# 1.45
# 21.40

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

    print("Rainfall Summary")
    print(f"Average rainfall {totalRain/days:4.2f}mm")  # 5.2f
    print(f"No of days with no rain {noRainDays} days")
    print(f"Highest rainfall recorded {max(dailyRain):5.2f}mm")

#Q1()

def Q1a():

    def main():
        print("Q1a main")
    
    main()

#Q1a()

def Q1c():

    def main():
        print("Q1c main")
    
    main()

#Q1c()

###### Those not covered were below Q4 and Q5

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
