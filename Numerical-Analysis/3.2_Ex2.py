from sympy import *


def main():
    x_list= [1]
    y_list = [-1]
    x = symbols('x')
    f = x**2 - 2
    df = diff(f, x)
    error = [1]
    while error[-1] > 10**(-3):
        x_list.append(float(x_list[-1] - f.subs(x, x_list[-1]) / df.subs(x, x_list[-1])))
        y_list.append(float(f.subs(x, x_list[-1])))
        error.append(abs(y_list[-1]-y_list[-2]))
    for i in range(len(x_list)):
        print('k={0} x={1:.15f} y={2:.15f} error={3:.15f}'.format(i, x_list[i], float(y_list[i]), error[i]))


main()
