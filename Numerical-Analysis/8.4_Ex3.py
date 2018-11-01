from sympy import *


def main():
    m = 6
    h = 0.2
    x_list = [0]
    y_list = [1]
    k = []
    for i in range(m):
        k.append([])
        k[i].append(fx(x_list[i], y_list[i]))
        k[i].append(fx(x_list[i] + h/2, y_list[i] + h/2 * k[i][0]))
        k[i].append(fx(x_list[i] + h/2, y_list[i] + h/2 * k[i][1]))
        k[i].append(fx(x_list[i] + h, y_list[i] + h * k[i][2]))
        x_list.append(x_list[-1] + h)
        y_list.append(y_list[i] + h / 6 * (k[i][0] + 2 * k[i][1] + 2 * k[i][2] + k[i][3]))
    for i, item in enumerate(k):
        print('{0} {1} {2} {3}'.format(i, item, x_list[i], y_list[i]))


def fx(a, b):
    x, y = symbols('x y')
    f = x + y
    ans = f.subs([(x, a),(y, b)])
    return ans


main()
