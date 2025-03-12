f = open('19481.txt')
mn = []
c = 0
for i in f:
    c += 1
    a = sorted([int(x) for x in i.split()])
    a_raz = [x for x in a if a.count(x) == 1]
    if len(a_raz) == 4:
        if (a[0] + a[3])**2 > (a[1]**3 + a[2]**3):
            mn.append(c)
print(sum(mn))
