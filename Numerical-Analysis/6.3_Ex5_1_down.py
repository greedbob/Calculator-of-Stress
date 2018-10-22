import math


def main():
    num = 1
    x = [0.7, 0.9, 1.1, 1.3, 1.5, 1.7]
    x.reverse()
    y = []
    fn = []
    for i in x:
        y.append(fx(i))
    fn.append(y)
    down_diff(fn)
    (ans, t) = inter(num, x, fn)
    for i in fn:
        print((len(fn[0]) - len(i)), ':', i)
    print('t is : {0}'.format(t))
    print('Ans is : {0}'.format(ans))


def fx(n):
    ans = math.sin(n)  # 改为原函数
    return ans


def down_diff(fn):
    for i in range(len(fn[0]) - 1):
        fn.append([])
        for j in range(len(fn[0]) - i - 1):
            temp = fn[-2][j] - fn[-2][j+1]
            fn[-1].append(temp)


def inter(num, x, fn):
    ans = 0
    for i in range(len(fn[0])):
        temp = fn[i][-1] / math.factorial(i)
        t = (x[-1] - num) / (x[1] - x[0])
        for j in range(i):
            temp *= t
            t = t + 1
        ans += temp
    return ans, t


main()
