from itertools import product, repeat

a = product('12345678', repeat=9)
c = 0
for i in a:
    num = ''.join(i)
    if num.count('1') <= 3 and num.count('2') <= 3 and num.count('3') <= 3 and num.count('4') <= 3 and num.count('5') <= 3 and num.count('6') <= 3 and num.count('7') <= 3 and num.count('8') <= 3:
                for j in '02468':
                    num = num.replace(j,'*')
                for l in '1357':
                    num = num.replace(l,'-')
                if '--' not in num and '**' not in num:
                    c += 1
print(c)