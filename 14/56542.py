for p in range(10, 36):
    for x in range(p):
        for y in range(p):
            num1 = 8*p**0 + x*p**1 + x*p**2 + x*p**3
            num2 = 9 * p ** 0 + x * p ** 1 + 3 * p ** 2 + 4 * p ** 3
            num3 = 4 * p ** 0 + 0 * p ** 1 + y * p ** 2 + y * p ** 3
            if num1 + num2 == num3:
                res = x*p**0 + y*p**1 + y*p**2
print(res)