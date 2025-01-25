f = open('9_17968.txt')

mn = []
mx = []
c = 0
for i in f:
    a = [int(x) for x in i.split()]
    a_n = sum([x for x in a if x % 2 == 0])
    a_d = sum([x for x in a if x % 2 != 0])
    if max(a) < sum(a) - max(a):
            if a_n == a_d:
                c += 1
print(c)
