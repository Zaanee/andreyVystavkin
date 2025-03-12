from string import ascii_uppercase
alph = '0123456789' + ascii_uppercase[:8]

for x in alph:
    num1 = int('11H' + x + '05',18)
    num2 = int('3F' + x + '54' + x + '8',18)
    num3 = int('G' + x + x + x + '9',18)
    res = num1 + num2 + num3
    if res % 14 == 0:
        print(res//14)