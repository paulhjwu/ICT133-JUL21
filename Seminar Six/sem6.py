

def Q3(): # Lab6(1)-1

    soups = {"Clam Chowder": 0, "Mushroom": 0, "Tomato": 0, "Pumpkin": 0, "Oxtail": 0}
    def getMenu():
        return int(input('''1.  Purchase Soup
2.  Replenish Soup
3.  List Soup
0.  Exit 
Enter your Choice '''))

    def printStock(soups):
        print(f"Soup           Portions")
        for item in soups.items():
            print(f"{item[0]:<15s}{item[1]:<78}")

    def purchaseSoup(soups):
        printStock(soups)
        soupToPurchase = input(f"Which soup to purchase? ")
        
        if soupToPurchase in soups:
            quantity = int(input(f"How many portions would be purchased? "))

            possibleQuantity = quantity if quantity <= soups[soupToPurchase] else soups[soupToPurchase] 

            if quantity > possibleQuantity:
                print(f"Only {possibleQuantity} out of {quantity} {soupToPurchase} can be purchsed!")
                print(f"{quantity - possibleQuantity} of {soupToPurchase} cannot be purchased!")
                soups[soupToPurchase] = 0
            else: 
                print(f"{quantity} of {soupToPurchase} are  purchased")
                soups[soupToPurchase] -= quantity
        else:
            print(f"Soup not found!!")

    def replenishSoup(soups):
        printStock(soups)
        soupToReplenish = input(f"Which soup to replenish? ")
        if soupToReplenish in soups:
            quantity = int(input(f"How many portions would be replinished? "))
            soups[soupToReplenish]+=quantity
        else: 
            print(f"Soup not found!!")

    choice = getMenu() 
    while True:
        
        if choice == 0: break

        if choice == 1:
            purchaseSoup(soups)
        elif choice == 2:
            replenishSoup(soups)
        elif choice == 3:
            printStock(soups)

        choice = getMenu()
Q3()