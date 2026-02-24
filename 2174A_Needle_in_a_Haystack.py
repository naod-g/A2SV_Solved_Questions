from collections import Counter

t = int(input())

for _ in range(t):
    s = list(str(input()))
    t = list(str(input()))
    res = []

    s_freq = Counter(s)
    t_freq = Counter(t)

    for x in s:
        if s_freq[x] > t_freq[x]:
            print("Impossible")
            break
    else:
        for ch in t:
            if s_freq[ch] > 0 and t_freq[ch] > 0:
                s_freq[ch] -= 1
                t_freq[ch] -= 1

        # all ch in t wothout ch in s
        t_s = [k*v for k, v in sorted(t_freq.items())]
        t_s = list("".join(t_s))

        res = []
        s_pointer = 0
        ts_pointer = 0

        while s_pointer < len(s) and ts_pointer < len(t_s):
            if t_s[ts_pointer] < s[s_pointer]:
                res.append(t_s[ts_pointer])
                ts_pointer += 1
            else:
                res.append(s[s_pointer])
                s_pointer += 1

        res.extend(s[s_pointer:])
        res.extend(t_s[ts_pointer:])

        print("".join(res))



