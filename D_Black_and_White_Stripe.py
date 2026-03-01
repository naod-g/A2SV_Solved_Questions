from collections import defaultdict

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n , k = list_()
    s = input()

    left = 0
    window = defaultdict(int)


    for i in range(k):
        window[s[i]] += 1
    res = window["W"]

    for right in range(k, n):
        window[s[right]] += 1
        window[s[left]] -= 1
        left += 1

        res = min(res, window["W"])

    print(res)
