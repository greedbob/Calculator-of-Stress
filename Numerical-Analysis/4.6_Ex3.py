err = 10
x = []
i = 0
x1 = x2 = x3 = 0
temp1 = temp2 = temp3 = 0
while err > 10 ** -4:
    x1 = 0.1 * x1 + 0.9 / 5 * (-12 - x3 - 2 * x2)
    x2 = 0.1 * x2 + 0.9 / 4 * (20 - 2 * x3 + x1)
    x3 = 0.1 * x3 + 0.9 / 10 * (3 + 3 * x2 - 2 * x1)
    if i > 0:
        err = max(abs(temp1 - x1), abs(temp2 - x2), abs(temp3 - x3))
    temp1 = x1
    temp2 = x2
    temp3 = x3
    i += 1
    x.append((i, x1, x2, x3, err))
    print(x[-1])


