def f(x,y,z):
    if x == y:
        return 1
    elif x > (y + 2):
        return 0
    else:
        if z[-2:] == 'aa':
            return f(x + 5,y,z + 'b') + f(x * 2,y,z + 'c')
        else:
            return f(x - 1, y, z + 'a') + f(x + 5, y, z + 'b') + f(x * 2,y,z + 'c')
print(f(5,34,''))