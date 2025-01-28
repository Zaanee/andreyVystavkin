for p in range(6,37):
    for q in range(6,37):
            num1 = 1*p**0 + 5*p**1 + 3*p**2 + 4*p**3 + 2*p**4
            num2 = 5 * q ** 0 + 2 * q ** 1 + 3 * q ** 2 + 4 * q ** 3 + 1 * q ** 4
            if int(num1) == int(num2):
                print(num1)

