for i in range(100000000):
    if ( i%3 == 0) and (i % 4 == 1) and (i % 5 == 3) and (i % 6 == 3) and (i % 7 == 0) and (i % 8 == 1) and (i % 9 == 0):
        print(i)
        break
else:
    print("The number is too great")
       
