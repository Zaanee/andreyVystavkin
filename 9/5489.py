f = open('5489.txt')

c = 0
for i in f:
    a = sorted([int(x) for x in i.split()])
    a_dif = [x for x in a if a.count(x) == 1]
    a_ch = [x for x in a_dif if x % 2 == 0]
    a_nch = [x for x in a_dif if x % 2 != 0]
    if len(a_dif) == 5:
        if len(a_ch) > len(a_nch):
            if sum(a_ch) < sum(a_nch):
                c+=1
print(c)
