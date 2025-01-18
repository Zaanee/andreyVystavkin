f = open('107_17.txt')
a = [int(x) for x in f]

p = []
s = []
for i in a:
    if i % 21 == 0:
        p.append(i)
p = min(p)
for i in range(len(a) - 1):
    k = [a[i], a[i + 1]]
    if k[0] % p == 0 or k[1] % p == 0:
        s.append(sum(k))
print(len(s),max(s))