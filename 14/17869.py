def f(n):
    s = []
    while n > 0:
        s.append(n % 25)
        n //= 25
    return s

num = 3*3125**8 + 2 * 625**7 - 4 * 625**6 + 3*125**5 - 2 * 25**4 - 2025
sis = f(num)
print(sis.count(0))