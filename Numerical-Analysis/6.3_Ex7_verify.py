from sympy import *


def main():
    x_list = [0, 1, 2]
    ans = [[], []]
    x = symbols('x')
    f0 = (x-2)**2 * x**2 - x**2 * (x-1) * (x-2) + 1/4 * x**2 * (x-1)**2
    sim_f0 = simplify(f0)
    print('Simplify f0 : {0}', sim_f0)
    f1 = df(sim_f0)
    for i in x_list:
        ans[0].append(f0.subs(x, i))
        ans[1].append(f1.subs(x, i))
    print(ans)


def df(f0):
    x = symbols('x')
    diff_y = diff(f0, x)
    return diff_y


main()
