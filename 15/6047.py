mn = []
for a in range(0,500):
    flag = True
    for x in range(0,500):
        for y in range(0, 500):
            f = (x > a) or (y > a) or (y - 2*x + 12 != 0)
            if f == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        mn.append(a)
print(max(mn))

