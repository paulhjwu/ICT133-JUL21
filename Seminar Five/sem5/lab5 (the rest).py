
def Q3():
    
    tutGp = {'T01': 28, 'T02':15, 'T03':28, 'T04':25, 'T05':29, 'T06':22 }

    def printSummary(tutGp): # Q3a 

        print(f"TG Size")

        size = 0
        for item in tutGp.items():
            print(f"{item[0]:<4s}{item[1]:<4d}")
            size += int(item[1])
        print(f"Total number of students {size}")   

    def updateTutGp(tutGp): # Q3b

        gp = input("Enter tutoral group: ")
        if gp in tutGp.keys():
            print(f"Tutorial group exists. Class size is {tutGp[gp]}")
            delta = int(input("Enter size to add/subtract group: "))
            tutGp[gp]+=delta
        else:
            delta = int(input("Enter class size: "))
            tutGp[gp]=delta
    
    def increaseByThree(tutGrp):

        for k, v in tutGrp.items():
            v = int(v)
            if v + 3 > 30:
                print(f"{k} adjusted to max 30")
            else:
                print(f"{k} adjusted to {v+3}")

    printSummary(tutGp)
    updateTutGp(tutGp)
    increaseByThree(tutGp)
    print(tutGp)

Q3()

def Q2b():

    def displayGameScore(gameScore):
        
        playerA = gameScore[0][0]
        playerB = gameScore[0][1]
        print(f"Player {playerA} vs {playerB}")
        
        a = 0
        b = 0

        for index, item in enumerate(gameScore[1:]):
            print(f"Game {index+1} {item[0]}-{item[1]}")
            if item[0]>item[1]:
                a+=1
            else:
                b+=1

        print(f"Overall {a}-{b}")

        if a > b:
            print(f"Winnder is player {playerA}")
        else:    
            print(f"Winnder is player {playerB}")

    def getPlayerNames():

        players = []
        for i in range(2):
            player = input(f"Player {i+1} name is ")
            players.append(player)
        
        return [ players ]


    def inputGameScores(coreList):

        count = 1
        while True:
            scores=input(f"Game {count} score {scoreList[0][0]} vs {scoreList[0][1]} ")
            if scores == "": break
            score1, score2 = scores.split("-")
            count+=1
            scoreList.append([score1, score2])
    
    scoreList = getPlayerNames()
    inputGameScores(scoreList)
    displayGameScore(scoreList)

#Q2b()

def Q2a():

    gameScore1=[['A','B'],[21,11],[19,21],[20,21]]
    gameScore2=[['A','B'],[21,1],[21,10]]

    def displayGameScore(gameScore):
        
        playerA = gameScore[0][0]
        playerB = gameScore[0][1]
        print(f"Player {playerA} vs {playerB}")
        
        a = 0
        b = 0

        for index, item in enumerate(gameScore[1:]):
            print(f"Gmae {index} {item[0]}-{item[1]}")
            if item[0]>item[1]:
                a+=1
            else:
                b+=1

        print(f"Overall {a}-{b}")

        if a > b:
            print(f"Winnder is player {playerA}")
        else:    
            print(f"Winnder is player {playerB}")

    displayGameScore(gameScore1)
    displayGameScore(gameScore2)


#Q2a()

def Q1c():

    # https://www.programiz.com/python-programming/examples/transpose-matrix

    scores_in = [[7.9,8.0,9.0,9.0,8.5,9.7],[7.8,8.5,9.1,9.2,8.8,9.8],[8.2,8.4,9.5,9.2,9.0,9.7]]
    scores_out = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]

    for i in range(len(scores_in)):

        for j in range(len(scores_in[i])):
            scores_out[j][i] = scores_in[i][j]

    def  Q1a(scores): 
        # a.
        a1 = "A1"
        a2 = "A2"
        a3 = "A3"
        total = "Total"
        print(f"Driver {a1:<4s}{a2:<4s}{a3:<4s}{total:<5s}")

        for index, aList in enumerate(scores):
            print(f"{index:^7d}", end="")
            sum = 0.0
            
            for i in range(len(aList)):
                print(f"{aList[i]:<4.1f}", end="")
                sum += aList[i]
            
            print(f"{sum:<5.1f}")
    
    Q1a(scores_out)

#Q1c()

def Q1b():

def 
    # b.
    total = "Total"
    print(f"Driver {total:<5s}")

    def keyFunc(elem):
        return elem[1]

    def totalScores(scores):
    
        aTotalList = []

        for index, aList in enumerate(scores):
            
            sum = 0.0 
            
            for i in range(len(aList)):
                sum += aList[i]
            
            aTotalList.append([index+1, sum])
        
        return aTotalList 

    aTotalList = totalScores(scores)

    aTotalList.sort(key=keyFunc, reverse=True)

    for index, item in enumerate(aTotalList[:3]):
         print(f"{item[0]:^7d}{item[1]:<4.1f}")

#Q1b()

def Q1a():

    scores=[[7.9,7.8,8.2],[8.0,8.5,8.4],[9.0,9.1,9.5], [9.0,9.2,9.2],[8.5,8.8,9.0],[9.7,9.8,9.7]]

    # a.
    a1 = "A1"
    a2 = "A2"
    a3 = "A3"
    total = "Total"
    print(f"Driver {a1:<4s}{a2:<4s}{a3:<4s}{total:<5s}")

    for index, aList in enumerate(scores):
        print(f"{index:^7d}", end="")
        sum = 0.0
        
        for i in range(len(aList)):
            print(f"{aList[i]:<4.1f}", end="")
            sum += aList[i]
        
        print(f"{sum:<5.1f}")

#Q1a()