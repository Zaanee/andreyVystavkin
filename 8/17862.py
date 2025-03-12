from itertools import product, repeat
c = 0
a = product('0123456789ab',repeat=5)
for i in a:
    num = ''.join(i)
    if num[0] != '0':
        if num.count('7') == 1:
            for j in '9ab':
                num = num.replace(j,'*')
            if num.count('*') <= 3:
                c += 1
print(c)