from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
nums = list_()

window = defaultdict(int)
length = float("-inf")
resl = None
resr = None
left = 0

for right in range(n):
    window[nums[right]] += 1

    while len(window) > k:
        window[nums[left]] -= 1
        if window[nums[left]] == 0:
            del window[nums[left]]
        left += 1

    if right - left > length:
        length = right - left
        resl = left + 1
        resr = right + 1

print(resl ,resr)
