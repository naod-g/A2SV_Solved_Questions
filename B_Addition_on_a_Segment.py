def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

n = int(input())

for i in range(n):
    k = int(input())
    b = list_()

    total = sum(b)
    best = 0

    for num in b:
        if num != 0:
            best += 1

    while best > 0:
        if total - best >= k-1:
            print(best)
            break
        else:
            best -= 1
        

