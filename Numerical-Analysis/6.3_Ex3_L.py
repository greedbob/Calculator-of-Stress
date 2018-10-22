import math


def main():
    num = 0.5
    x = [0, 0.3, 0.6]
    y = []
    for i in range(len(x)):
        y.append(fx(x[i]))
    temp = lagrange_inter(num, x, y)
    print(temp)


def fx(n):
    ans = math.e ** (2 * n) * math.cos(3 * n)  # 改为原函数
    return ans


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