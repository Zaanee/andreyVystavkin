f = open('17_16383.txt')
a = [int(x) for x in f]
mn = []
ms = []
c = 0
for j in a:
    if (j % 100 == 21) and len(str(abs(j))) == 5:
        mn.append(j)
for i in range(len(a) - 1):
    k = [a[i], a[i+1]]
    k_usl = [x for x in k if len(str(abs(x))) == 5 and str(x)[-2:] == '21']
    if len(k_usl) == 1:
        if k[0]**2 + k[1]**2 >= (max(mn))**2:
            ms.append(sum(k))
            c += 1
print(c,max(ms))
