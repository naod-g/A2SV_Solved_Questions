def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n, k = list_()
    total = k
    arr = []

    for i in range(n):
        arr.append(list_())

    arr.sort(key = lambda x: x[0])

    for l, r, real in arr:
        if l <= total <= r and real > total:
            total = real

    print(total)
