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

Q2()


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