def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())
contests = sorted(list_())

day = 1

for contest in contests:
    if contest >= day:
        day += 1
print(day - 1)
