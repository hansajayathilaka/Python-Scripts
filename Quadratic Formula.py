while True:
    print ("ax^2 + bx + c")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    if ((b**2)-(4*a*c)) >= 0:
        A = (((-1)*b)+((b**2)-(4*a*c))**(1/2))/(2*a)
        B = (((-1)*b)-((b**2)-(4*a*c))**(1/2))/(2*a)
        print ("Roots of the formula are (",A ,") and (",B ,(")"))
    else:
        print ("???")
    print ("========================================================")
    input()
