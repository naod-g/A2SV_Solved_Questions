from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
nums = list_()

left = right = count = 0
window = defaultdict(int)

for right in range(n):
    window[nums[right]] += 1

    while len(window) > k:
        window[nums[left]] -= 1
        if window[nums[left]] == 0:
            del window[nums[left]]
        left += 1
    count += right - left + 1
    

print(count)
