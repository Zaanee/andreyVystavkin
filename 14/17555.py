def f(n):
    s = []
    while n > 0 :
        s.append(n % 7)
        n //= 7
    return s

mn = [0]
for x in range(1,2030):
    num = 7**91 + 7**160 - x
    sis = f(num)
    if sis.count(0) == 70:
        mn.append(x)
    print(max(mn))

