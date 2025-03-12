def dl(n,m):
    if n % m == 0:
        return True
    else:
        return False
mn = []
for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        f = dl(70,a) and (dl(x,28) <= ((not dl(x,a)) <= (not dl(x,21))))
        if f == 0:
            flag = False
            break
    if flag == True:
        mn.append(a)
print(max(mn))