import math

def reg(eq):
    if 'x**2' in eq:
        return 2
    elif 'x' in eq:
        return 1
    else:
        return 0

def begin(eq):
    eq_value = reg(eq)
    if eq_value == 2:
        sqr(eq)
    if eq_value == 1:
        ln(eq)
    if eq_value == 0:
        print('это не уравнение')



def sqr(eq):
    eq = eq.split()
    d = int(eq[4])**2 - 4*int(eq[0])*int(eq[-1])

    if d >= 0:
        x1 = (-(int(eq[4])) + d**0.5)/2*int(eq[0])
        x2 = (-(int(eq[4])) - d**0.5)/2*int(eq[0])
        if x1 + x2 == -(int(eq[4])) and x1 * x2 == int(eq[-1]):
            print(math.trunc(x1),math.trunc(x2))
            return x1,x2
    else:
        print('нет корней')
        return 'undefined'
def ln(eq):
    eq = eq.split()
    x = -(int(eq[4]))/int(eq[0])
    if int(eq[0])*x + int(eq[4]) == 0:
        print(math.trunc(x))
        return x

eq = input()
begin(eq)




