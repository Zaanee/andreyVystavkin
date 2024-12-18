f = open('16375.txt')
c = 0

for i in f:
    a = [int(x) for x in i.split()]
    a_sec = [x for x in a if a.count(x) == 2]
    a_n = sorted([x for x in a if a.count(x) == 1])
    if len(a_sec) == 2 and len(a_n) == 5:
        if a_n[0] * a_n[1] * a_n[2] > (a_sec[0])**2:
            c+=1
print(c)