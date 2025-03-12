import sys
sys.setrecursionlimit(10**6)

def f(n):
    if n == 0:
        return 0
    if n > 0:
        if n % 2 == 0:
            return f(n // 2)
    if n % 2 != 0:
        return 1 + f(n - 1)
mn = []
for i in range(1,100000):
    if f(i) == 12:
        mn.append(i)
print(min(mn))
