def f(n):
    s = []
    while n > 0:
        s.append(n % 7)
        n //= 7
    return s
mn = []
for x in range(1,2031):
    num = 7**170 + 7**100 - x
    sis = f(num)
    if sis.count(0) == 71:
        mn.append(x)
print(max(mn))