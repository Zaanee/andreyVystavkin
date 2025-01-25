def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
mn = []
for n in range(1,1000):
    b = f(n)
    if n % 3 == 0:
        b = b + b[-2:]
    else:
        su = sum(map(int,list(b)))
        b = b + f(su)
    r = int(b, 3)
    if r > 220:
        if r % 2 == 0:
           mn.append(r)
print(min(mn))

