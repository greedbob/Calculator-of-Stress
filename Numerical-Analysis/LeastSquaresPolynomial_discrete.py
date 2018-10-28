# 离散点的任意阶最小二乘法
# code by Bo on 10/28/2018

from sympy import *


def main():
    n = 1
    x_list = []  # x 值列表
    fx = []  # f(x) 值列表
    y = []
    para = parameter(n)
    poly(n, x_list, fx, y, para)
    result = solve(y, para)
    P = Px(para, result)
    print('P{0} is: {1}'.format(n, P))
    E = error(x_list, fx, P)
    print('Error{0} is: {1}'.format(n, E))


def parameter(n):
    para = []
    for i in range(n+1):
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


def Px(para, result):
    x = symbols('x')
    P = x*0
    for i, key in enumerate(para):
        P += result[key] * x**i
        i += 1
    return P


def error(x_list, fx, P):
    E = 0
    x = symbols('x')
    for i in range(len(fx)):
        E += (fx[i] - P.subs(x, x_list[i]))**2
    return E


main()
