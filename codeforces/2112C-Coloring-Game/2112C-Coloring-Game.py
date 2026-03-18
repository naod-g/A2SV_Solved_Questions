import bisect
def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    a = list_()
    res = 0

    for i in range(n):
        for j in range(0, i):
            x = max(a[-1], 2*a[i]) - a[i] - a[j]
            k = bisect.bisect_right(a, x, hi=j)

            res += (j-k)

    print(res)

    # bob = a[-1]
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             curr = a[i] + a[j] + a[k]
    #             change = max(2 * a[k], a[-1])
    #             if curr > change:
    #                 res += 1

    # print(res)