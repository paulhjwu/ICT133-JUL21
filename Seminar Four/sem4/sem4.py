<<<<<<< HEAD
def double(x):
    x = x.append(2)
    z = x
    return z

def main():
    z = [1]
    x = [10]
    y = double(x)
    print(x, y)

main()
=======

def slide21():

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    maxMonths = [ monthName[index]  if month[index] == max(month) ]

    print(maxMonths)

slide21()


def slide18_20():

    month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    monthName = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    maxDays= max(month)

    for index in range( 12):
      print(f"Month {index+1} has {month[index]} days.")
      if month[index] == maxDays:
          print(f"Month {monthName[index]} has maximun days")
    
    if 29 in month:
        print('Leap year')
    else:
        print('Not a leap year')

#slide18_20()

def slide16():

    myList = [34, 26, 15, 10]
    myList[2] = 12

    myTuple = (34, 26, 15, 10)
    print(myTuple[2])
    #myTuple[2] = 12

    print("")

#slide16()

def slide13_15():

    for elem in [1, 2, 'Ann', 3.3]:
        print (elem, end=" ")
    print("")
    
    # t1 = [1, 2]
    # t2 = [3 ]

    t1 = (1, 2)
    t2 = (3, )

    print(t1 + t2)
    print(t2 * 5)

#slide13_15()


def slide9():

    type(3)
    type(3.0)
    myInt = 5
    myFloat = 3.0
    type(myInt)
    type(myFloat)

    print("")

#slide9()


def slide8():

    fileName = input("What file are the numbers in? ")
    dataDirectoryPath= "data"
    dataFile = dataDirectoryPath + "/" + fileName
    infile = open(dataFile,'r')

    sum, count = 0.0, 0

    all_text = infile.read()

    for line in all_text.split('\n'):
        if line != '':
            for xStr in line.split(","):
                
                sum = sum + float(xStr)
                count = count + 1

    print("\nThe average of the numbers is", sum/count)
    infile.close()

#slide8()

def slide7():

    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')

    sum, count = 0.0, 0
    
    for line in infile:
        for xStr in line.split(","):

            sum = sum + float(xStr)
            count = count + 1

    print("\nThe average of the numbers is", sum/count)
    infile.close()

#slide7()

def slide6():

    fileName_in = input("What file are the numbers in? ")
    fileName_out = input("What file is to store the results? ")

    infile = open(fileName_in,'r')
    outfile = open(fileName_out,'w')
    
    sum, count = 0.0, 0
    
    for line in infile: # lines separated by \n  
    
        sum = sum + float(line)
        count = count + 1
    
    print(f"\nThe average of the numbers is {sum/count}", file=outfile)

    infile.close()
    outfile.close()

#slide6()

def slide3():

    str = "Hello\nWorld\n\nGoodbye 32\n"
    print(str)

#slide3()

def slide0():
    txt = "I like bananas"

    x = txt.replace("bananas", "apples")

    print(x)

    print(txt[0], txt[1], txt[2])

    aList = [1, 2, 3]

    print(aList[0], aList[1], aList[2])

    aList[1]=4
    print(aList)

    #txt[1]='b'
    x = txt.replace(' ', 'b')

    print("")

#slide0()
>>>>>>> 4a3fb47a3823a1f103b9c304bac337e672127b8a
