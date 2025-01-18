f = open('17.txt')
a = [int(x) for x in f]

s = []

for i in range(len(a) - 1):
    k = [a[i], a[i + 1]]
    if k[0] % 3 == 0 or k[1] % 3 ==0:
        if (k[0] + k[1]) % 5 == 0:
            s.append(k[0] + k[1])
print(len(s), max(s))
