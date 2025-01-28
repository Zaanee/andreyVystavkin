def f(n):
    s = []
    while n > 0:
        s.append(n % 7)
        n //= 7
    return s
num1 = 7**21 + 49**13 - 7**10
print(f(num1).count(6))

