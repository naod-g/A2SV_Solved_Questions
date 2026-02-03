def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    a, b, n = list_()
    tools = list_()

    res = b

    for tool in tools:
        if tool < a:
            res += tool
        else:
            res += a - 1

    print(res)
