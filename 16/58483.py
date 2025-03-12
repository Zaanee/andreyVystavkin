import sys
sys.setrecursionlimit(10**6)
c = 0
def f(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n + f(2 * n)
def g(n):
    return f(n)//n
for n in range(1,100000):
    if g(n) == g(1000):
        c += 1
print(c)
