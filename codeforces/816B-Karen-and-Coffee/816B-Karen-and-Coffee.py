def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k, q = list_()
recipes = [list_() for _ in range(n)]
questions = [list_() for _ in range(q)]

# compute the max value in all
mx = 0
for a,b in recipes:
    if a > b:
        if a > mx:
            mx = a
    else:
        if b > mx:
            mx = b
for a,b in questions:
    if a > b:
        if a > mx:
            mx = a
    else:
        if b > mx:
            mx = b

pre = [0] * (mx + 2)

for a,b in recipes:
    pre[a] += 1
    pre[b+1] -= 1

for i in range(1, mx+2):
    pre[i] += pre[i-1]

for i in range(mx+2):
    pre[i] = 1 if pre[i] >= k else 0

for i in range(1, mx+2):
    pre[i] += pre[i-1]

for a, b in questions:
    print(pre[b] - pre[a-1])