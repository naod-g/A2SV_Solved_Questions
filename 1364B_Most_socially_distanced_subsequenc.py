def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list_()
    res = [nums[0]]

    for i in range(1, n-1):
        if (nums[i-1] < nums[i]) != (nums[i] < nums[i+1]):
            res.append(nums[i])
    res.append(nums[n-1])

    print(len(res))
    print(*res)
