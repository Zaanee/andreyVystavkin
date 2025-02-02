mn = []
for n in range(1,1000):
    m = 278
    a = bin(m)[2:]
    b = bin(n)[2:]
    if len(a) > len(b):
        while len(a) > len(b):
            b = b + '0'
    if len(a) < len(b):
        while len(a) < len(b):
            a = a + '0'
    r = (a or b)
    if r.count('1') == 7:
        mn.append(n)
print(r,min(mn))