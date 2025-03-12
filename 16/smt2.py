import sys
sys.setrecursionlimit(10**6)
c = 0
def f(n):
    if n == 0:
        return 0
    if n > 0:
        if n % 2 == 0:
            return f(n // 2)
    if n % 2 != 0:
        return 1 + f(n - 1)
for i in range(1,500):
    if f(i) == 8:
        c += 1
print(c)
