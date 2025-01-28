for x in '012356789abc':
    num1 = int('753' + x + '2', 13)
    num2 = int( '2' + x + '173', 13)
    res = num1 + num2
    if res % 12 == 0:
        print(x,res//12)
