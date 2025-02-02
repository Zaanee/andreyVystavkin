from fnmatch import fnmatch
for n in range(4891,10**10,4891):
    if fnmatch(str(n),'1?7602*0'):
        print(n)

