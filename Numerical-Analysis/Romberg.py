from sympy import *


def main():
    T = [[]]
    m = 4
    x = symbols('x')
    fx = 4/(1+x**2)
    a, b = (0, 1)
    Trapezoid(a,b,m,fx,T)
    for i in range(m):
        T.append([])
        for j in range(m - i):
            T[i+1].append((4**(i+1)/(4**(i+1)-1)*T[i][j+1] - 1/(4**(i+1)-1)*T[i][j]))
    print(T)


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
