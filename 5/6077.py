mn = []
for n in range(100,1000):
    for i in range(100,1000):
        k = [n, i]
        sot = int(str(k[0])[0]) + int(str(k[1])[0])
        des = int(str(k[0])[1]) + int(str(k[1])[1])
        ed = int(str(k[0])[2]) + int(str(k[1])[2])
        ks = str(ed) + str(sot) + str(des)
        if len(ks) == 3:
            ksu = '0' + ks[0:1]
            if ksu == '002':
                mn.append(k[0])
        if len(ks) == 4:
            ksu = ks[0:-2]
            if ksu == '002':
                mn.append(k[0])
        if len(ks) == 5:
            ksu = ks[1:-2]
            if ksu == '002':
                mn.append(k[0])
        if len(ks) == 6:
            ksu = ks[2:-2]
            if ksu == '002':
                mn.append(k[0])
print(max(mn))


