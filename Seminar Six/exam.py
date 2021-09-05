def Q3():

    #Q3a
    
    from random import randrange # 1 mark
    def getRandomNumber(minimum, maximum): # 1 mark:
        return randrange(minimum, maximum + 1) # 1 mark
    
    #Q3b
    def getRandomAverage(times, minimum, maximum): # 1 mark
        
        total = 0 # 1 mark
        
        for _ in range(times): # 1 mark
            total += getRandomNumber(minimum, maximum) # 1 mark
        
        return total/times # 1 mark

    #Q3c
    def checkRandomness(times, precision, minimum, maximum): # 1 mark
    
        outfile = open('randomnessCheck.txt', 'a') # 1 mark
        ave1 = round(getRandomAverage(times, minimum, maximum), precision) # 2 marks
        ave2 = round((minimum + maximum)/2, precision) # 2 marks

        print(f'Average of {times} random numbers, {ave1} is {"the same as" if ave1 == ave2 else "different from"} average of {minimum} and {maximum}, {ave2}') # 1 mark
        print(f'Average of {times} random numbers, {ave1} is {"the same as" if ave1 == ave2 else "different from"} average of {minimum} and {maximum}, {ave2}', file=outfile) # 2 marks
        
        outfile.close()# 1 mark

    #Q3d
    def main():

        minimum, maximum = input('Enter the minimum value and maximum values, separated by a space: ').split() # 1 mark
        minimum, maximum = int(minimum), int(maximum) # 1 mark
        precision = int(input('Enter number of digits precision after decimal point: ')) # 1 mark
    
        while True: # 1 mark
            times = int(input('Enter number of random numbers to test: ')) # 1 mark
            if times <= 0: # 1 mark
                break
            checkRandomness(times, precision, minimum, maximum) # 1 mark
    
        print('Application ended')
    
    main()

#Q3()

def Q4():

    def claim(insurance): # 1 mark

        outfile = open('claims.txt', 'a')
        pType = input('Enter policy type: ') # 1 mark
        
        if pType not in insurance: # 1 mark
            print('Invalid policy type')
        else:
            amount = float(input('Enter claim amount: $')) # 1 mark
            if amount <= 0: # 1 mark
                print('Invalid claim amount') 
            else:
                insurance[pType].append(amount) # 2 marks
                print('Successful policy claim') # 1 mark

    def summary(insurance):

        print('Summary of Policies A, B, C')  # 1 mark`
        print('Policy  Total Claimed($)  Number of Claims') # 1 mark
        
        for k,v in insurance.items():# 2 marks
            print(f'{k:^6}  {float(sum(v)):15.2f}  {len(v):>17}')  # 3 marks
        
        print('End Summary') # 1 mark    

    def getOption():# 1 mark
        return int(input('''Menu
1.    Make A Claim
2.    Get Summary
0.    Exit
Enter option: '''))
        
    def main():
        insurance = {'A': [], 'B': [], 'C': []} # 1 mark
        while True: # 2 marks
            option = getOption()# 1 mark
            if option == 1: # 1 mark
                claim(insurance)
            elif option == 2: # 1 mark
                summary(insurance)
            elif option == 0: # 1 mark
                break
            else: # 1 mark
                print('Invalid option')
        print('Application ended')
        
    main() 

Q4()

def LabQ3():

    soups = {"Clam Chowder": 50, "Mushroom": 50, "Tomato": 50, "Pumpkin": 50, "Oxtail": 50}

    def displayMenu():
        return int(input('''1. Purchase Soup
2. Replenish Soup
3. Print Stock
0. Exit 
Enter your choice '''))

    def keyFunc(elem):
        return elem[0]

    def printStock(soups):

        menu = []

        for item in soups.items():
            menu.append(list(item))
        
        menu.sort(key=keyFunc)

        for elem in menu:
            if elem[1] >= 0:
                print(f"Soup {elem[0]} has {elem[1]} servings left")
        
    def purchaseSoup(soups):

        printStock(soups)  
        soupToPurchase = input("Which soup to be purchased ")

        if soupToPurchase in soups:

            quantity = int(input(f"How many portions would be purchased? "))

            possibleQuanity = quantity if quantity <= soups[soupToPurchase] else soups[soupToPurchase]

            if quantity > possibleQuanity :
                print(f"Only {possibleQuanity} out of {quantity} {soupToPurchase} can be purchased")
                print(f"{quantity - possibleQuanity } of {soupToPurchase} cannot be purchased")
                soups[soupToPurchase] = 0
            else:
                print(f"{quantity} of {soupToPurchase} are purchased")
                soups[soupToPurchase] -= quantity
        
        else:
            print(f"Soup not found!!")

        return soups
    
    def replenishSoup(soups):

        printStock(soups)

        soupToReplenish = input(f"Which soup to be replenished? ")
        if soupToReplenish in soups:
            quantity = int(input(f"How many portions would be replenished? "))
            soups[soupToReplenish] += quantity
        else:
            print(f"Soun not found in the Stock")


    #displayMenu()
    #purchaseSoup(soups)
    #print(soups)
    #replenishSoup(soups)
    #print(soups)

    choice = displayMenu()

    while True:
    
        if choice == 0: break

        if choice == 1:
            purchaseSoup(soups)
        elif choice == 2:
            replenishSoup(soups)
        elif choice == 3:
            printStock(soups)

        choice = displayMenu()

#LabQ3()


# Quesiton 1.b
def f(s):

    n = 0 

    x = 0

    while x < len(s):

        if int(s[x]) % 2 == 0: 
            n += 1
        x += 1

    return n

# def f(s):

#     n = 0 

#     for c in range(len(s)): 
#         if int(s[c]) % 2 == 0: 
#             n += 1

#     return n

#print(f('162534'))

#Qustion 1a i and ii

def subtract(x, y):

    z = 0

    if x < y :
        buffer = x
        x = y
        y = buffer
        swopped = True

    while x > y:
        x -= 1
        z += 1

    if not swopped:
        print(z)
    else:
        print(-z)

#subtract(2, 3)