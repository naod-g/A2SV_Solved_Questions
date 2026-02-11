t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    p0 = 0
    p1 = 0
    pos = 0
 
    for i in range(n):
        pos += 1 if s[i] == 'R' else -1
 
        if pos == -x and not p0:
            p0 = i + 1
        if pos == 0 and not p1:
            p1 = i + 1
 
    if p0:
        if p1:
            zeros = (k - p0) // p1 + 1
        else:
            zeros = 1
    else:
        zeros = 0
 
    print(zeros)
