from sympy import *


def main():
    T = [[]]
    m = 5
    x = symbols('x')
    fx = x**1.5
    a, b = (0, 1)
    Trapezoid(a,b,m,fx,T)
    for i in range(m):
        T.append([])
        for j in range(m - i):
            T[i+1].append((4**(i+1)/(4**(i+1)-1)*T[i][j+1] - 1/(4**(i+1)-1)*T[i][j]))
    for i in range(len(T[0])):
        for j in range(len(T[0])-i):
            print(T[j][i], end=' ')
        print()


def Trapezoid(a, b, m, fx, T):
    x = symbols('x')
    for j in range(m+1):
        n = 2**j
        h = (b - a) / n
        T[0].append([])
        for i in range(n):
            if i == 0:
                T[0][j] = h/2*(fx.subs(x,a)+fx.subs(x,b))
            else:
                T[0][j] += h*fx.subs(x, i*h)


main()
