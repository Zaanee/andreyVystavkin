

for x in range(37):
    num1 = 15*37**0 + 8*37**1 + 9*37**2 + 10*37**3 + 11*37**4 + x*37**5 + 9*37**6 + 5*37**7 + 12*37**8
    num2 = 6*37**0 + 12*37**1 + 9*37**2 + 10*37**3 + 13*37**4 + 5*37**5 + x*37**6 + 3*37**7 + 14*37**8
    res = num1 * num2
    if res % 36 == 0:
        num3 = 1*37**0 + x*37**1 + 2*37**2
        print(x,num3)