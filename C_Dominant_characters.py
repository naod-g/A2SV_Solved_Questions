t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    mn = float('inf')

    for i in range(n):
        for j in range(i+2, min(n, i+7) + 1):
            sub = s[i: j]
            count_a = sub.count("a")
            count_b = sub.count("b")
            count_c = sub.count("c")

            if count_a > count_b and count_a > count_c:
                mn = min(mn, j - i)

    print(mn if mn !=  float('inf') else -1)


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = input()

#     sub_strings = []

#     for x in range(n):
#         for y in range(x+1, n):
#             sub_strings.append(s[x:y+1])

#     sub_strings.sort(key = lambda x: (len(x), x))

#     for ss in sub_strings:
#         if len(ss) >= 2 and ss.count("a") > ss.count("b") and ss.count("a") > ss.count("c"):
#             print(len(ss))
#             break
#     else:
#         print(-1) 
