def f(m):
    s = ''
    while m > 0:
        s = str(m % 7) + s
        m //= 7
    return s

c = 0
for n in range(343,2402):
    b = f(n)
    if int(b[-1]) % 2 == 0:
        b = '6' + b
    else:
        b = '5' + b
    r = int(b,7)
    if r > 14500:
        c+=1
print(c)
