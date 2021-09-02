def Q5():

    marks = { 'John':[90,90], 'Jane':[20,40], 'Peter':[90,90], 'Joe':[90,90] }

    def menuGetOption():

        return int(input('''
Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Exit 
Enter your option: '''
))

    #menuGetOption()

    def addMarks(marks):

        name = input("Enter Name : ")

        if marks.get(name):
            print(f"Student already exists")
        else:
            work = float(input(f"Enter course work makrs : "))
            exam = float(input("Enter exam marks : "))
            marks[name]=[work, exam]
            print("Added")
    
    #addMarks(marks)
    
    def updateMarks(marks):

        name = input("Enter Name : ")

        sMarks = marks.get(name)
        
        if  sMarks == None:
            print(f"Student does not have marks yet")
        else:
            print(f"({name} found, marks displayed)")
            print(f"Course work: {sMarks[0]}")
            print(f"Exam: {sMarks[1]}")

            part = input(f"Update C or E: ")

            if part == 'C':
                c = float(input(f"Enter course work: "))
                sMarks[0] = c
                print(f"Course work adjusted to {c}")
            else:
                e = float(input(f"Enter exam : "))
                sMarks[1] = e
                print(f"Exam work adjusted to {e}")

    #updateMarks(marks)
    
    def removeMarks(marks):

        name = input("Enter Name : ")
    
        sMarks = marks.get(name)

        if sMarks == None:
            print(f"Student not found")
        else:
            marks.pop(name)
            print(f"{name} is removed")

    #removeMarks(marks)

    def displayMarks(marks):

        print(f"Name    Cw      Ex      Overall Grade")
        for key, item in marks.items():
            print(f"{key:<8s}{item[0]:<8.2f}{item[1]:<8.2f}{'P' if (item[0]*0.5 + item[1]*0.5 ) >= 50 else 'F'}")

    #displayMarks(marks)
    
    option = menuGetOption()
    print("The option chosen is {option}")  

    while option != 0:
        
        if option == 1:
            addMarks(marks)
        elif option == 2:
            updateMarks(marks)
        elif option == 3:
            removeMarks(marks)
        elif option == 4:
            displayMarks(marks)

        option = menuGetOption()
        print(f"The option chosen is {option}")   

    print(marks)

Q5()