from math import gcd

def nok(a,b):
    return (a*b) / gcd(a,b)



l = nok(354,648)
from fnmatch import fnmatch

for n in range(l,10**10,l):
    if fnmatch(str(n),'21?5846*?'):
        print(n, n // 2025)