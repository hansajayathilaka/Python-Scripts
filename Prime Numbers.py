x = 0
c = 0
while x < 1000000:
    y = 2
    a = 0
    while x > y:
        if (x % y) != 0:
            a = 1
        else:
            a = 0
            y = x
        y = y + 1
    if a == 1:
        print (x)
        c = c + 1
    x = x + 1
print ("Count of Prime Numbers = " , c)

