def main():
    num = 2
    x = [1.7, 1.8, 1.9, 2.1]
    y = []
    fn = []
    for i in x:
        y.append(fx(i))
    fn.append(y)
    fn = fnx(x, fn)
    print(fn)
    N = Nx(num, x, fn)
    print(N)


def fx(x):
    return (4 * x - 7)/(x - 2)


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
        print(i+1)
        inter = 1
        for j in range(i+1):
            if j == 0:
                inter *= fn[i+1][0]
            inter *= num - x[j]
        ans += inter
    return ans


main()