from itertools import product, repeat

a = product('0123456789ab',repeat=6)
c = 0
for i in a:
    num = ''.join(i)
    if num[0] != '0':
        if num.count('b') == 1:
            for j in '02468a':
                num = num.replace(j,'*')
            for l in '13579b':
                num = num.replace(l,'-')
            if num.count('*') == num.count('-'):
                c += 1
print(c)






















