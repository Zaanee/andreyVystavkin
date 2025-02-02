import sys
sys.setrecursionlimit(10**6)

def f(n):
    if n > 1000000:
        return n
    else:
        return n + f(2 * n)
def g(n):
    return f(n)//n
c = 0
for i in range(1,10000):
    if g(i) == g(1000):
        c += 1
print(c)
