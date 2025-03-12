mn = []
for a in range(500):
    flag = True
    for x in range(500):
        f = (x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))
        if f == 0:
            flag = False
            break
    if flag == True:
        mn.append(a)
print(min(mn))