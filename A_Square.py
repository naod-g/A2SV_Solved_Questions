def list_(): return list(map(int, input().split()))

n = int(input())
for i in range(n):
    nums = list_()
    if len(set(nums)) == 1:
        print("YES")
    else:
        print("NO")