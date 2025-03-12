def f(x,y,z):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        if z.count('C') > 2:
            return f(x + 1,y,z + 'A') + f(x + 2,y,z + 'B')
        else:
            return f(x + 1,y,z + 'A') + f(x + 2,y,z + 'B') + f(x * 2,y,z + 'C')
print(f(2,12,''))