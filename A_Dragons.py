from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

s, n = list_()

mp = defaultdict(int)

for strength in range(n):
    strength, point = list_()
    mp[strength] += point

strkey = sorted(mp.keys())

flag = False
for k in strkey:
    if s > k:
        s += mp[k]
        flag = True
    else:
        flag = False


if flag:
    print("YES")
else:
    print("NO")

