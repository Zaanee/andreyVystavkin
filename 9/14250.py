f = open('14250.txt')
s = []
c = 0
for i in f:
    a = [int(x) for x in i.split()]
    a_dif = sorted([x for x in a if a.count(x) == 1])
    c += 1
    if len(a_dif) == 6:
        if (a_dif[-1] - a_dif[0])**3 >= (a_dif[1] + a_dif[2] + a_dif[3] + a_dif[4])**2:
            s.append(c)
print(sum(s))