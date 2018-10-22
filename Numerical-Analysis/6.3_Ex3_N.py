import math


def main():
    num = 0.5
    x = [0, 0.3, 0.6]
    y = []
    fn = []
    for i in x:
        y.append(fx(i))
    fn.append(y)
    fn = fnx(x, fn)
    print(fn)
    N = Nx(num, x, fn)
    print(N)


def fx(n):
    ans = math.e ** (2 * n) * math.cos(3 * n)  # 改为原函数
    return ans


def fnx(x, fn):
    for i in range(len(x)-1):
        fn.append([])
        for j in range(len(x)-i-1):
            ans = (fn[i][j+1] - fn[i][j])/(x[i+j+1]-x[j])
            fn[i+1].append(ans)
    return fn


def Nx(num, x, fn):
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
