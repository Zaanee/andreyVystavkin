f = open('17_2.txt')
a = [int(x) for x in f]

p = []
s = []
for i in a:
    if i % 2 == 0:
        p.append(i)
for i in range(len(a) - 1):
    k = [a[i], a[i + 1]]
    if (k[0] % 3 == 0 and k[1] < sum(p)/len(p)) or (k[1] % 3 == 0 and k[0] < sum(p)/len(p)):
            s.append(sum(k))
print(len(s),max(s))