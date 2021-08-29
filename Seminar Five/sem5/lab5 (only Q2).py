def Q2d():

    scoreList = []

    #Q2.b
    def getPlayerNames():

        scoreList = []
        playerNameList = []

        for i in range(2):
            player = input(f"Player {i+1} name is ")
            playerNameList.append(player)

        scoreList.append(playerNameList) 
        
        return scoreList
    
    #Q2.c
    def inputGameScores(scoreList):

        # scoreList = [[A, B] , [xxx, yyyy]]

        # Game 1 score A vs B: 21-10
        # Game 2 score A vs B: 21-11
        # Game 3 score A vs B: <enter> key to represent end of input

        game = 0

        while True:
            scores = input(f"Game {game+1} score {scoreList[0][0]} vs {scoreList[0][1]}: ")
            if scores == "": break
            score1, score2 = scores.split('-')
            scoreList.append([score1, score2])
            game += 1

    #Q2.a
    def displayGameScore(gameScore):

        # This function is meant to print the game results according to the specification.
        # Once printed, done. So, no need to have output (no return statement is needed)

        a = 0
        b = 0

        # Player A vs B
        print(f"Player {gameScore[0][0]} vs {gameScore[0][1]}")

        # Game 1 21-11
        # Game 2 19-21
        # Game 3 11-21

        for index, item in enumerate(gameScore[1:]):
            print(f"Game {index+1} {item[0]}-{item[1]}")
            if item[0] > item[1]:
                a += 1
            else:
                b += 1

        # Overall 1-2
        print(f"Overall {a}-{b}")

        # Winner is player B
        if a > b:
            print(f"Winnder is player {gameScore[0][0]}")
        else:
            print(f"Winnder is player {gameScore[0][1]} ")

    # Call Q2.b
    scoreList = getPlayerNames()
    
    # Call Q2.c
    inputGameScores(scoreList)

    # Call Q2.a
    displayGameScore(scoreList)

Q2d()

def Q2c():

    scoreList = [['A', 'B']]

    def inputGameScores(scoreList):

        # scoreList = [[A, B] , [xxx, yyyy]]

        # Game 1 score A vs B: 21-10
        # Game 2 score A vs B: 21-11
        # Game 3 score A vs B: <enter> key to represent end of input

        game = 0

        while True:
            scores = input(f"Game {game+1} score {scoreList[0][0]} vs {scoreList[0][1]}: ")
            if scores == "": break
            score1, score2 = scores.split('-')
            scoreList.append([score1, score2])
            game += 1

    inputGameScores(scoreList)
    print(scoreList)

#Q2c()

def Q2b():

    scoreList = []

    def getPlayerNames():

        scoreList = []
        playerNameList = []

        for i in range(2):
            player = input(f"Player {i+1} name is ")
            playerNameList.append(player)

        scoreList.append(playerNameList) 
        
        return scoreList
    
    scoreList = getPlayerNames()
    print(scoreList)

#Q2b()
        
def Q2a():
    
    gameScore1=[['A','B'],[21,11],[19,21],[20,21]]
    gameScore2=[['A','B'],[21,1],[21,10]]

    def displayGameScore(gameScore):

        # This function is meant to print the game results according to the specification.
        # Once printed, done. So, no need to have output (no return statement is needed)

        a = 0
        b = 0

        # Player A vs B
        print(f"Player {gameScore[0][0]} vs {gameScore[0][1]}")

        # Game 1 21-11
        # Game 2 19-21
        # Game 3 11-21

        for index, item in enumerate(gameScore[1:]):
            print(f"Game {index+1} {item[0]}-{item[1]}")
            if item[0] > item[1]:
                a += 1
            else:
                b += 1

        # Overall 1-2
        print(f"Overall {a}-{b}")

        # Winner is player B
        if a > b:
            print("Winnder is player A")
        else:
            print("Winnder is player B")
        
        #return ????

    displayGameScore(gameScore1)
    displayGameScore(gameScore2)

    #print(f"The first element of the first element is {gameScore[0][0]}")

#Q2a()
