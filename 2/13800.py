print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not((x == y) or (y == w) or (w == z)) or (x and (not y))
                if int(f) == 1:
                        print(x,y,z,w,int(f))




#xwzy