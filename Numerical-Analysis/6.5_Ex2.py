from sympy import *


def main():
    n = 2
    x = symbols('x')
    a, b = (0 ,1)
    fx = 1/2 * cos(x) + 1/3 * sin(2*x)
    y = []
    para = parameter(n)
    poly(n, a, b, x, fx, y, para)
    result = solve(y, para)
    print(result)
    P = Px(para, result)
    print('P{0} is: {1}'.format(n, P))
    E = error(a, b, fx, P)
    print('Error{0} is: {1}\nError{0} is: {2}'.format(n, E, float(E)))


def parameter(n):
    para = []
    for i in range(n+1):
        para.append(symbols('a{0}'.format(i)))
    return para


def poly(n, a, b, x, fx, y, para):
    for j in range(n+1):
        y.append(0*x)
        for k in range(n+2):
            if k != n+1:
                y[j] += para[k]*integrate(x**(j+k), (x, a, b))
            else:
                y[j] -= float(integrate(x**j * fx, (x , a, b)))
        print('y{0} = '.format(j), y[-1])


def Px(para, result):
    x = symbols('x')
    P = x*0
    for i, key in enumerate(para):
        P += float(result[key]) * x**i
        i += 1
    return P


def error(a, b, fx, P):
    x = symbols('x')
    E = integrate((fx - P)**2,(x, a, b))
    return E


main()
