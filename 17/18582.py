f = open('17_18582.txt')
a = [int(x) for x in f]
mn = []
ms = []
c = 0
for j in a:
    mn.append(j)
for i in range(len(a) - 2):
    k = [a[i], a[i+1], a[i+2]]
    k_dif = [x for x in k if x < 0]
    su = sum(k)
    if len(k_dif) >= 2:
        if str(su)[-1:] == str(min(mn))[-1:]:
            c += 1
            ms.append(abs(su))
print(c, max(ms))



















































