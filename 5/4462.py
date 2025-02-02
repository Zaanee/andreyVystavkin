mn = []
for n in range(2,1000):
    b = bin(n)[2:]
    b = b.replace('1','',1)
    co = b.count('1')
    if co % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '0'
    r = int(b, 2)
    if r < 450:
        mn.append(r)
print(max(mn))