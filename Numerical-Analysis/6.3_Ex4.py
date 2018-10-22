import math


def main():
    num = 1  # 输入要计算的插值点
    x = [0.9, 1.1]  # 输入自变量序列
    y = []  # 给出原函数而非因变量序列时使用fx()函数计算因变量序列，给出因变量序列可不运行fx函数
    fn = []
    for i in x:
        y.append(fx(i))
    fn.append(y)
    fn = fnx(x, fn)
    for i in fn:  # 输出各阶差分
        print(len(x) - len(i), ':', i)
    ans = newton_inter(num, x, fn)
    print(ans)  # 输出插值


def fx(n):
    ans = math.sin(n)  # 改为原函数
    return ans


def fnx(x, fn):
    for i in range(len(x)-1):
        fn.append([])
        for j in range(len(x)-i-1):
            ans = (fn[i][j+1] - fn[i][j])/(x[i+j+1]-x[j])
            fn[i+1].append(ans)
    return fn


def newton_inter(num, x, fn):
    ans = 0
    ans += fn[0][0]
    for i in range(len(x)-1):
        inter = 1
        for j in range(i+1):
            if j == 0:
                inter *= fn[i+1][0]
            inter *= num - x[j]
        ans += inter
    return ans


main()
