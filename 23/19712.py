def f(x,y,z):
    if x == y:
        return 1
    if x < y:
        return 0
    if x > y:
        if z[-2:] == 'AA':
            if x % 2 == 0:
                return  f(x / 2,y,z + 'B')
            else:
                return f(x - 7,y,z + 'B')
        elif z[-2:] == 'BB':
            if x % 2 == 0:
                return  f(x - 2,y,z +'A')
            else:
                return f(x - 2,y,z + 'A')
        else:
            if x % 2 == 0:
                return f(x - 2, y, z + 'A') + f(x / 2,y,z + 'B')
            else:
                return f(x - 2, y, z + 'A') + f(x - 7,y,z + 'B')

print(f(40,1,''))