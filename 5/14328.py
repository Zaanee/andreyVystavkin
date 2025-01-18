from string import ascii_uppercase

alph = '0123456789' + ascii_uppercase


def f(n):
    s = ''
    while n > 0:
        s = alph[n % 12] + s
        n //= 12
    return s
mx = []
for n in range(1,1000):
    b = f(n)
    if n % 3 == 0:
        b = '1' + b + 'B'
    else:
        b = '2' + b + '0'
    r = int(b, 12)
    if r < 1996:
        mx.append(r)
print(max(mx))


        #if n % 12 == 10:
        #     s = 'A' + s
        # elif n % 12 == 11:
        #     s = 'B' + s
        # else:
        #     s = str(n % 12) + s


#s = hex(n % 12)[2:] + s