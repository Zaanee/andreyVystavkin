def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
mn = []
for n in range(1,1000):
    b = f(n)
    if n % 7 == 0:
        b = b + b[-2:]
    else:
        b = b + f((n % 7)*3)
    r = int(b, 3)
    if r > 369:
        mn.append(r)
print(min(mn))