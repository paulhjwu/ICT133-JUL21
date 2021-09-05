def Q3():

    #Q3.a
    from random import randrange
    def getRandomNumber(min, max):
        return randrange(min, max+1)

    #Q3.b
    def getRandomAverage(min, max, times):
        sum = 0

        for i in range(times):
            sum +=  getRandomNumber(min, max)
        
        return sum/times
    
    #Q3.c
    def checkRandomness(min, max, times, precision):
        
        theAverage = round( (min + max) /  2, precision)
        theRandomAverage=round(getRandomAverage(min, max, times), precision)

        print(f"Average of {times} random numbers between {min} and {max}, {theRandomAverage}, is \
{'different from' if theAverage != theRandomAverage else 'the same as'} \
the (ideal) average, {theAverage}")


    #Q3.d
    def main():

        min, max=input(f"Enter the minimum value and maximum values, separated by a space: " ).split()
        min = int(min)
        max = int(max)
        precision = int(input(f"Enter number of digits precision after decimal point: "))
        times = int(input(f"Enter number of random numbers to test: "))

        while times != -1:
            checkRandomness(min, max, times, precision)
            min, max=input(f"Enter the minimum value and maximum values, separated by a space: " ).split()
            min = int(min)
            max = int(max)
            precision = int(input(f"Enter number of digits precision after decimal point: "))
            times = int(input(f"Enter number of random numbers to test: "))
    
    main()  
    #checkRandomness(1, 20, 1000000, 2)

#Q3()

def Q4():

    def claim(insurance):

        outfile = open("claims.txt", 'a')
        pType = input("Enter policy type: ")

        if pType not in insurance:
            print("Invalid policy type")
        else:
            amount = float(input("Enter claim amount: $"))
            if amount <= 0:
                print("Invalid claim amount")
            else:
                insurance[pType].append(amount)
                print('Successful policy claim')
                print(f"{pType} {amount}", file=outfile)

    def summary(insurance):

        print("Summary of Policies A, B, C")
        print("Policy   Total Claimed($)   Number of Claims")

        for k, v in insurance.items():
            print(f"{k:<9}${sum(v):<18.2f}{len(v):<10}")

        print("End Summary")

    def getOption():

        return int(input('''Menu
1. Make A Claim
2. Get Summary
0. Exit
option:'''))
             
    def main():

        insurance = {'A': [], 'B': [], 'C': []}

        while True: 
            option = getOption()
            if option == 1:
                claim(insurance)
            elif option == 2:
                summary(insurance)
            elif option == 0:
                break
            else:
                print("Invalid Option")
        
        print("Applicaiton ends")


    #claim(insurance)
    #summary(insurance)
    main()
    print("")

Q4()

def Q2():

    def larger(a, b):
        return a if a > b else b

    def largest(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if theLargest < aList[i]:
                theLargest = aList[i]
        return theLargest
    
    students = {'John': 53, 'Ann': 62, 'Peter':45, 'Tom':62}


    scoreList=list(students.values())
    largestScore = largest(scoreList)
    
    #b.1
    print(f"The largest score is {largestScore}")

    #b.2
    studentNames = [name for name, value in students.items() if value==largestScore]
    print(f"The students with largest score is/are: {studentNames}")

    #b.3
    print(f"Number of students scoring {largestScore} is {len(studentNames)}")

    #c
    def secondLargest(aList):

        # make a copy of aList
        # find the largest of (copy of) aList
        # remove the largest from aList
        # find the largest of the remaining list

        anotherList=aList.copy()
        #anotherList = aList
        theLargest = largest(anotherList)
        anotherList.remove(theLargest)
        theSecondLargest = largest(anotherList)

        return theSecondLargest

    aList=[2, 5, 1, 6]
    print(secondLargest(aList))
    print(largest(aList))
    print("")


#Q2()


def slide3():

    class Person:

        def __init__(self, name, age):
            self.name = name
            self.age = age

    def doSomething(x, y, w):
        x[0]=9
        z = y.replace('t', 'g')
        w.age=37
        return z

    def main():
        a = [10, 11, 12]
        b = 'ant'
    
        p = Person("John", 36)
        print(f"{p.name} is {p.age} years old")
    
        c = doSomething(a, b, p)

        print(f"{c}")
        #p.age = 37
        print(f"{p.name} is {p.age} years old") # a[idx], a[key], a.key

        print("")

    main()

#slide3()