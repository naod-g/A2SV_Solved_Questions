def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    s = input()
    i = 0
    res = set()

    while i + 1 < len(s):
        if s[i] == s[i+1]:
            i += 2
        else:
            res.add(s[i])
            i += 1

    if i == len(s) - 1:
        res.add(s[i])

    print("".join(sorted(res)))
