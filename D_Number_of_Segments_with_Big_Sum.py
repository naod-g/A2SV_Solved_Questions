def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, s = list_()
nums = list_()

left = 0
sm = 0
count = 0

for right in range(n):
    sm += nums[right]

    while sm >= s:

        count += (n - right)
        sm -= nums[left]
        left += 1

print(count)
        
