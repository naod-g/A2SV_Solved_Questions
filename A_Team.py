def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())
res = 0

for _ in range(n):
    arr = list_()

    if arr.count(1) >= 2:
        res += 1
print(res)
