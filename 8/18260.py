from itertools import product

a = product('0123456789ab',repeat=6)
c = 0
for s in a:
    num = ''.join(s)
    if num[0] != '0':
        if num.count('b') == 1:
            for j in '13579b':
                num = num.replace(j,'-',)
            for g in '02468a':
                num = num.replace(g,'+')
            if num.count('-') == num.count('+'):
                c += 1
print(c)