def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input())
    b = list(input())

    zeros = once = 0
    can_flip = [False] * n

    for i in range(n):
        if a[i] == '1':
            once += 1
        else:
            zeros += 1
    
        if once == zeros:
            can_flip[i] = True


    flip = False

    for i in range(n-1,-1,-1):
        bit = a[i]
        if flip:
            bit = '1' if bit == '0' else '0'  # inverting the bit
        if bit == b[i]:
            continue
        if not can_flip[i]:
            print("NO")
            break
        flip = not flip

    else:
        print("YES")