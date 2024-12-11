for a in range(50,121):
    flag = True
    for x in range(1,1000):
        f = (x & a == 0) <= ((x & 31 != 0) <= (x & 35 != 0))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)