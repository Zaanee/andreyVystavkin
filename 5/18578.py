def f(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s
mn = []
for i in range(1,1000):
    b = f(i)
    if i % 4 == 0:
        b = '2' + b + '03'
    else:
        b = b + f((i % 4)*5)
    r = int(b, 4)
    if r <= 567:
        mn.append(i)
print(max(mn))
