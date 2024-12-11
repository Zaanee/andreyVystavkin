for a in range(1,500):
    flag = True
    for x in range(1,500):
        for y in range(1, 500):
            f = (7 * y + x < a) or (2*x + 3*y > 98)
            if f == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)