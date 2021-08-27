def slide11():

    month = {'January': 31, 'February': 28, 'March': 31, \
    'April': 30, 'May': 31, 'June': 30, \
    'July': 31, 'August': 31, 'September': 30,\
    'October': 31, 'November': 30, 'December': 31}

    month['February']=29

    for key, value in month.items():
        print(f"{key} has {value} days")

    #print(f"Janary has {month['January']} days")

slide11()


def slide8():

    def getScores():

        scores = []

        while True:
            name = input( 'Enter name: ').capitalize()
            if name == '': break
            score = int(input( 'Enter score: '))
            scores.append([name, score])

        return scores

    scores = getScores()

    name = input('Enter the name to search for score: ')

    for nameScore in scores:
        if nameScore[0] == name:
            print(f"{name}'s score is {nameScore[1]}")
            break
    else:
        print(f"{name} has no score record")

#slide8()

def slide7_2():

    def getScores():
        
        scores = []
        names = []

        while True:
            name = input( 'Enter name: ').capitalize()
            if name == '': break
            names.append(name)
            score = int(input( 'Enter score: '))
            scores.append(score)

        return names, scores

    def byScore(elem):
        return elem[1]

    def printScore(scores):
        for nameScore in scores:
            print(f"{nameScore[0]} scores {nameScore[1]} points")
    
    names, scores = getScores()
    #scores.sort(key=byScore, reverse=True)
    zipStuff=list(zip(names, scores))
    zipStuff.sort()
    printScore(zipStuff)

#slide7_2()

def slide7():

    def getScores():

        scores = []

        while True:
            name = input( 'Enter name: ').capitalize()
            if name == '': break
            score = int(input( 'Enter score: '))
            scores.append([name, score])

        return scores

    def byScore(elem):
        return elem[1]

    def printScore(scores):
        for nameScore in scores:
            print(f"{nameScore[0]} scores {nameScore[1]} points")
    
    scores = getScores()
    #scores.sort(key=byScore, reverse=True)
    scores.sort()
    printScore(scores)

#slide7()


def slide4():

    month = [['January', 31], ['February', 28], ['March', 31], \
    ['April', 30], ['May', 31], ['June', 30], \
    ['July', 31], ['August', 31], ['September', 30],\
    ['October', 31], ['November', 30], ['December', 31]]

    month[1][1]=29

    for m in month:
        print(f'{m[0]} has {m[1]} days')

#slide4()

def slide3():

    month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    monthName = ( 'January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December')

    #i, name = (0, 31)

    for i, name in enumerate(monthName):
        print(f'{name} has {month[i]} days')

    zipStuff = zip(month, monthName)

    for dayName in zip(month, monthName):
        print(f'{dayName[1]} has {dayName[0]} days ')

    for days, name in zip(month, monthName):
        print(f'{name} has {days} days ')

#slide3()
