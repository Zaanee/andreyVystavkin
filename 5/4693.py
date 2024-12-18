mn = []
for n in range(1,1000):
    b = bin(n)[2:]
    su = sum(map(int,list(b)))
    if su % 2 == 0:
        b = '10' + b[2:] + '0'
    if su % 2 != 0:
        b = '11' + b[2:] + '1'
    r = int(b,2)
    if r > 40:
        mn.append(n)
print(min(mn))