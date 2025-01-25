
for n in range(10, 1000):
    d = []
    for i in range(len(str(n)) - 1):
        d.append(str(n)[i] + str(n)[i + 1])
        d = list(map(int, d))
        print(d)
        mx = max(d)
        mn = min(d)
        res = mx - mn
        if res == 44:
            print(n)
            break
