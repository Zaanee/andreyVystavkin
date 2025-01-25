from string import ascii_uppercase

alph = '0123456789' + ascii_uppercase[:15]
for x in alph:
    num1 = int('11353' + x + '12',25)
    num2 = int('135' + x + '21',25)
    res = num1 + num2
    if res % 24 == 0:
        print(res // 24)

