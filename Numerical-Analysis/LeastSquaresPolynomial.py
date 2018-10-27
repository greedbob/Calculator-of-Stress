from sympy import *


def main():
    n = 0
    x = []
    fx = []
    y = []
    para = parameter(x)
    poly(n, x, fx, y, para)
    result = solve(y, para)
    print(result)


def parameter(x):
    para = []
    for i in range(len(x)):
        para.append(symbols('a{0}'.format(i)))
    return para


def poly(n, x, fx, y, para):
    for i in range(n+1):
        y.append(0*para[0])
        for j in range(n+2):
            if j != n+1:
                temp = 0
                for jj in range(len(x)):
                    temp += x[jj]**(j+i)
                y[i] += para[j]*temp
            else:
                temp = 0
                for jjj in range(len(x)):
                    temp += fx[jjj]*x[jjj]**i
                y[i] -= temp
        print('y{0} = '.format(i), y[-1])


main()
