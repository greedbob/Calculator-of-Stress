from sympy import *


def main():
    x_list = [-(3/5)**0.5, 0, (3/5)**0.5]
    y = []
    x = symbols('x')
    fx = x**2 / (1 - x**2)**0.5
    for i in range(len(x_list)):
        y.append(float(fx.subs(x, x_list[i])))
    print(y)
    ans = 5/9 * y[0] + 8/9 * y[1] + 5/9 * y[2]
    print(ans)


main()