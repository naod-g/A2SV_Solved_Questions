def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    for i in range(n):

        a,b,c,d = list_()

        if a > c:
            res += (a - c)
        if b > d:
            res += (b - d) + min(a, c)
    print(res)