f = open('19700.txt')

c = 0
for i in f:
    a = sorted([int(x) for x in i.split()])
    a_pov = [x for x in a if a.count(x) == 2]
    a_raz = [x for x in a if a.count(x) == 1]
    if len(a_pov) == 2 and len(a_raz) == 3:
        if (a[0] + a[4]) < (a[1] + a[2] + a[3]):
            c += 1
print(c)
