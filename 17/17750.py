f = open('17_17750.txt')
a = [int(x) for x in f]
mn = []
ms = []
c = 0
for j in a:
    mn.append(j)
for i in range(len(a) - 1):
    k = [a[i], a[i+1]]
    if k[0] % 77 + k[1] % 77 == min(mn):
        ms.append(sum(k))
        c += 1
print(c,max(ms))