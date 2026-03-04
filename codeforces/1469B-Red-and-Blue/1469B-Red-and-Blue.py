def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    r = list_()
    m = int(input())
    b = list_()

    pre_red = [r[0]] * n
    pre_blue = [b[0]] * m

    for i in range(1, n):
        pre_red[i] = pre_red[i-1] + r[i]
    for i in range(1, m):
        pre_blue[i] = pre_blue[i-1] + b[i]

    res = 0
    if max(pre_blue) > 0:
        res += max(pre_blue)
    if max(pre_red) > 0:
        res += max(pre_red)
    print(res)