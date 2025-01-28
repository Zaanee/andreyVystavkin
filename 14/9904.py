for x in range(10,14):
    for y in range(9,x):
        num1 = int('7' + hex(x)[2:] + '37' + hex(y)[2:], 14)
        num2 = int('9' + hex(y)[2:] + '63', x)
        num3 = int('15148', y)
        res = num1 + num2 - num3
        su = x + y
        print(su, res // su)


