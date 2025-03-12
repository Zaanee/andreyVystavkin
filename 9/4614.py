f = open('4614.txt')
c = 0
for i in f:
    a = sorted([int(x) for x in i.split()])
    a_dif = [x for x in a if a.count(x) == 1]
    a_rv = [x for x in a if a.count(x) == 2]
    if len(a_rv) == 2 and len(a_dif) == 2:
        if a[3] < a[0] + a[1] + a[2]:
            c += 1
print(c)
