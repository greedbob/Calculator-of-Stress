def main():
    num = 0
    x = []
    y = []
    temp = lagrange_inter(num, x, y)
    print(temp)


def lagrange_inter(num, x, y):
    ans = 0
    l = []
    for i in range(len(x)):
        temp_l = 1
        for j in range(len(x)):
            if j != i:
                temp_l *= (num - x[j]) / (x[i] - x[j])
        l.append(temp_l)
        ans += l[-1] * y[i]
    return l, ans


main()