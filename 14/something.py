

for x in range(2,27):
    num1 = 1*27**0 + 3*27**1 + 7*27**2 + x*27**3 + 2*27**4 + 4*27**5
    num2 = 3 * 27 ** 0 + x * 27 ** 1 + 8 * 27 ** 2 + 9 * 27 ** 3 + x * 27 ** 4 + 5 * 27 ** 5
    num3 = 6 * 27 ** 0 + 2 * 27 ** 1 + 7 * 27 ** 2 + x * 27 ** 3 + 4 * 27 ** 4 + 9 * 27 ** 5
    res = num1 + num2 + num3
    if res % 26 == 0:
        print(x,res // 26)

# from string import ascii_uppercase
# a = '0123456789' + ascii_uppercase[:17]
#     num1 = int('42' + x + '731',27)
#     num2 = int('5' + x + '98' + x + '3',27)
#     num3 = int('94' + x + '726', 27)