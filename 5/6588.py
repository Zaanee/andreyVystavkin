mn = []
for n in range(1,1000):
    b = bin(n)[2:]
    b = b.replace('0',"*")
    b = b.replace('1', "+")
    b = b.replace('*', "1")
    b = b.replace('+', "0")
    b = '1' + b
    co = b.count('1')
    if co % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    r = int(b, 2)
    if r > 180:
        mn.append(n)
print(min(mn))
