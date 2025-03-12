def f(x,y,z):
    if x == y and z == 8:
        return 1
    if x > y or z == 8 or (x == y and z != 8):
        return 0
    if x < y:
            return f(x + 2,y,z + 1) + f(x + 4,y,z + 1) + f(x * 2,y,z + 1)
print(f(4,64,0))
