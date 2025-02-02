def f(n):
    s = []
    while n > 0:
        s.append(n % 4)
        n //= 4
    return s[::-1]

a = 4**644 + 4**322 + 16**35 - 64**3
sis = f(a)
print(sis.count(3))