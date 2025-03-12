print(bin(214)[2:].zfill(8),bin(96)[2:].zfill(8),bin(0)[2:].zfill(8),bin(0)[2:].zfill(8))
print(bin(255)[2:].zfill(8),bin(240)[2:].zfill(8),bin(0)[2:].zfill(8),bin(0)[2:].zfill(8))

from itertools import product
c = 0
a = product('01',repeat=20)
for i in a:
    ip = ''.join(i)
    if (ip.count('0') + 5) % 3 == 0:
        c += 1
print(c)