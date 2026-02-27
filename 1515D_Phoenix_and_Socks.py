from collections import Counter
def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n, l, r = list_()
    socks = list_()

    left = Counter(socks[:l])
    right = Counter(socks[l:])
    res = 0

    # if same socks are in both discard them, no chnage in res
    for ch in left.keys():
        m = min(left[ch], right[ch])
        left[ch] -= m
        right[ch] -= m
        l -= m
        r -= m
    # making the left always the greater for not to repeat
    if l < r:
        l, r = r, l
        left, right = right, left
    
    # Balance sides using duplicate colors
    diff = l - r
    for sock in list(left.keys()):
        pairs = left[sock] // 2
        use = min(pairs, diff // 2)
        left[sock] -= (use * 2)
        l -= (use * 2)
        res += use
        diff -= (2*use)

    # fix remaining imbalance Move remaining extra socks from left to right.
    diff = l - r
    l -= diff // 2
    r += diff // 2
    res += diff // 2


    # Recolor remaining unmatched socks
    res += l

    print(res)
