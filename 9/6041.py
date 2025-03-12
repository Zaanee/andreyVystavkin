f = open('6041.txt')
c = 0
for i in f:
    a = sorted([int(x) for x in i.split()])
    a_dif = [x for x in a if a.count(x) == 1]
    if len(a_dif) == 3:
        if a[2] < a[1] + a[0]:
            c += 1
print(c)