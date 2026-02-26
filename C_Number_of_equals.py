from collections import Counter
def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, m = list_()

a, b = list_(), list_()
count = 0
ac = Counter(a)
bc = Counter(b)

for k, v in bc.items():
    count += (v * ac[k])

print(count)
