# from string import ascii_uppercase
# a = ascii_uppercase
# c = 9
# for i in a:
#     c+=1
#     print(c,i)
for x in range(27):
    num1 = 5*27**0 + 3*27**1 + x*27**2 + 7*27**3 + 1*27**4
    num2 =  22* 27 ** 0 + 2 * 27 ** 1 + 4 * 27 ** 2 + 7 * 27 ** 3 + x * 27 ** 4
    num3 = x**3
    res = num1 + num2 + num3
    if res % 23 == 0:
        print(res//23)
