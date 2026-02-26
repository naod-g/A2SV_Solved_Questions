def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, s = list_()
nums = list_()

count = res = left = sm = 0

for right in range(n):
    sm += nums[right]
    count += 1

    while sm > s:
        sm -= nums[left]
        count -= 1
        left += 1

    res += count


print(res)
