mn = []
for n in range(2,10000):
    b = bin(n)[2:]
    c = 0
    c1 = 0
    c0 = 0
    for i in b:
        c += 1
        if c % 2 == 0:
            if i == '1':
                c1 += 1
        else:
            if i == '0':
                c0 += 1
    r = abs(c1 - c0)
    if r == 5:
        mn.append(n)
print(min(mn))





