while True:
    x = 0
    y = 2
    a = 0
    x = int(input ("Enter your Number "))
    while x > y:
        if (x % y) != 0:
            if a == 0:
                a = 1
            elif a == 2:
                a = 2
        else:
            a = 2
            print (y)
        y = y + 1
    if a == 2:
        print ("Above numbers are the factors of", x)
        print (x , "is not a prime number")
    else:
        print (x , "is a prime number")
    print("=========================================")
    input()
