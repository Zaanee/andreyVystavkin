from itertools import product, repeat

a = product('КАЙФ',repeat=4)
c = 0
for i in a:
    num = ''.join(i)
    if len(num) == len(set(num)):
        if num[-1] != 'Й':
            if 'КФ' not in num:
                c += 1
print(c)