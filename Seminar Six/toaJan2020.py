def Q1a():

    a, b = 16, 5
    c = 0
    while True:
        if a >= b:
            c = c + 1
            a = a - b
        else:
            break
    print(a, b, c)

    a, b = 16, 5
    c = 0

    print(f"{a % b} {b} {a//b}")

#Q1a()

def Q1b():

    s = 'abcdefgh'
    newS = ''
    for i in range(0, len(s), 3):
        newS += s[i].upper() + s[i+1:i+3]
        print(newS)

#Q1b()

def Q2a():

    def larger(a, b):
        return a if a > b else b
    
    def largest(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if theLargest < aList[i]:
                theLargest = aList[i]
        return theLargest
    
    def largest2(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if larger(theLargest, aList[i]) != theLargest:
                theLargest = aList[i]
        return theLargest

    test = [1, 5, 3, 4]
    print(largest(test))
    print(largest2(test))

#Q2a()

def Q2b():

    def largest(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if theLargest < aList[i]:
                theLargest = aList[i]
        return theLargest
    
    students = {'John':53, 'Ann':62, 'Peter':45, 'Tom':62}

    largestValue=largest(list(students.values()))
    names = [k for k, v in students.items() if v == largestValue]
    print(f"Largest Value = {largestValue} Names = {names}")

#Q2b()

def Q2c():

    def largest(aList):
        theLargest = aList[0]
        for i in range(1, len(aList)):
            if theLargest < aList[i]:
                theLargest = aList[i]
        return theLargest

    def secondLargest(aList):     
        y = aList.copy()
        theLargest = largest(y)
        z = [v for v in y if v != theLargest]
        return largest(z)

    aList = [2, 5, 1, 6]
    print(secondLargest(aList))
    print(largest(aList))

Q2c()