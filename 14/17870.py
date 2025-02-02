def f(n):
    s = 0
    while n > 0:
        if n % 7 == 0:
            s+=1
        n //= 7
    return s

for x in range(1,2031):
    a = 7**170 + 7**100 - x
    b = f(a)
    if b == 71:
        print(x)