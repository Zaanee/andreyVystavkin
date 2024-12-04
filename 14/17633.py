def f(n):
    s = []
    while n > 0:
        s.append(n % 6)
        n //= 6
    return s
mn = []
for x in range(1, 2030):
    num = 6**260 + 6**160 + 6**60 - x
    sis = f(num)
    if sis.count(0) == 202:
        mn.append(x)
print(min(mn))


