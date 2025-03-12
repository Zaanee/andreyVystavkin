print(bin(165)[2:].zfill(8),bin(44)[2:].zfill(8),bin(96)[2:].zfill(8),bin(0)[2:].zfill(8))
print(bin(255)[2:].zfill(8),bin(255)[2:].zfill(8),bin(248)[2:].zfill(8),bin(0)[2:].zfill(8))

from itertools import product
c = 0
a = product('01',repeat=11)
for i in a:
    ip = ''.join(i)
    if '111' in ip:
        c+=1
print(c)