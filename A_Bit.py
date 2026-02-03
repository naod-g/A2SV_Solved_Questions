def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

res = 0

n = int(input())
for _ in range(n):
    op = str(input())
    if op == "--X" or op == "X--":
        res -= 1
    else:
        res += 1
print(res)

