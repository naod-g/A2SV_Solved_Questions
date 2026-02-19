def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
nums = list_()
gaps = [nums[i] - nums[i-1] for i in range(1, n)]
gaps.sort(reverse = True)

print(nums[-1] - nums[0] - sum(gaps[:k-1]))
