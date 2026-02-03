def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n, k = list_()
scores = list_()
ref = scores[k-1]
advanced = 0

for score in scores:
    if score >= ref and score > 0:
        advanced += 1
print(advanced)

