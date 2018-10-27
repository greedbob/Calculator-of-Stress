from sympy import *


def main():
    x_list = [-(3/5)**0.5, 0, (3/5)**0.5]
    y = []
    x = symbols('x')
    fx = pi/4 * (1 - 1/2 * (sin(pi/4 * (x+1)))**2)**0.5
    for i in range(len(x_list)):
        y.append(float(fx.subs(x, x_list[i])))
    print(y)
    ans = 5/9 * y[0] + 8/9 * y[1] + 5/9 * y[2]
    print(ans)


main()