c = 0
for n in range(1,100000000):
    b = bin(n)[2:]
    b = b + bin(n % 3)[2:].zfill(2)
    b = b + bin(n % 5)[2:].zfill(3)
    r = int(b, 2)
    if 1111111110 <= r <= 1444444416:
        c += 1
print(c)