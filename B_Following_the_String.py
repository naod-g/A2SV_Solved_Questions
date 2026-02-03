from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for i in range(n):
    k = int(input())
    arr = list_()

    mp = defaultdict(int)
    curr = 97
    res = []
    
    for j in arr:
        if j == 0:
            res.append(chr(curr))
            mp[chr(curr)] += 1
            curr += 1
        else:
            for ch in sorted(mp):
                if mp[ch] == j:
                    res.append(ch)
                    mp[ch] += 1
                    break
    print("".join(res))