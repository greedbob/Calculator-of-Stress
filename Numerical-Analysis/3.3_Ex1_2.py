from sympy import *


def main():
    x_list= [1, 2]
    y_list = []
    x = symbols('x')
    f = x**3 - 3 * x -1
    y_list.append(f.subs(x, x_list[0]))
    y_list.append(f.subs(x, x_list[1]))
    error = [1, abs(y_list[-1] - y_list[-2])]
    while error[-1] > 10**(-4):
        x_list.append(float(x_list[-1] - f.subs(x, x_list[-1])*(x_list[-1] - x_list[-2])/
                            (f.subs(x, x_list[-1]) - f.subs(x, x_list[-2]))))
        y_list.append(float(f.subs(x, x_list[-1])))
        error.append(abs(y_list[-1]-y_list[-2]))
    for i in range(len(x_list)):
        print('k={0} x={1:.15f} y={2} error={3}'.format(i, x_list[i], float(y_list[i]), error[i]))


main()
