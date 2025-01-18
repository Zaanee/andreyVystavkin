def f(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s

mn = []
for m in range(1,1000):
    b = f(m)
    if m % 4 == 0:
        b = b + b[0:2]
    else:
         b = b + f((m % 4)*4)
    r = int(b, 4)
    if r > 291:
        mn.append(r)
print(min(mn))
