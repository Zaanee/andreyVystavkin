c = 0
for a in range(-500,500):
    flag = True
    for x in range(0,500):
        for y in range(0, 500):
            f = ((x < a) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= a))
            if f == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        c += 1
print(c)
