def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = 5
res = 0
desired = 2

for i in range(5):
    nums = list_()
    for j in range(5):
        if nums[j] == 1:
            res += abs(desired - i) + abs(desired - j)


print(res)