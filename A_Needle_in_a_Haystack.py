from collections import Counter

t = int(input())

for _ in range(t):
    s = list(str(input()))
    t = list(str(input()))
    res = []

    t_freq = Counter(t)
    s_freq = Counter(s)

    for key, val in s_freq.items():
        if t_freq[key] < val:
            print("Impossible")
            break

    else:
        t_freq -= s_freq
        t = []

        for key, val in t_freq.items():
            t.extend([key]*val)
        t.sort()

        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] <= t[j]:
                res.append(s[i])
                i += 1
            else:
                res.append(t[j])
                j += 1

        while j < len(t):
            res.append(t[j])
            j+= 1
        while i < len(s):
            res.append(s[i])
            i += 1
            
    print("".join(res))

    