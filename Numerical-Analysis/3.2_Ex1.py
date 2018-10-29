from sympy import *


def main():
    x = symbols('x')
    fx = x**3 - 2
    a = 1
    b = 2
    ans = []
    error = 10**(-3)
    n = int((log(b - a) - log(error))/log(2))
    for i in range(n):
        c = (a + b) / 2
        fa = fx.subs(x, a)
        fb = fx.subs(x, b)
        fc = fx.subs(x, c)
        if fa * fc < 0:
            ans.append([c, fc])
            b = c
        else:
            ans.append([c, fc])
            a = c
    for i, item in enumerate(ans):
        print(i+1, item)


main()
