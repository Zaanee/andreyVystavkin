mn = []
for n in range(1,10000000):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b + bin(5)[2:]
    else:
        b = b + '1'
    if int(b) % 7 == 0:
        b = b + bin(7)[2:]
    else:
        b = b + '1'
    r = int(b, 2)
    if r < 1728404:
        mn.append(n)
print(max(mn))