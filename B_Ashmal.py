def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n = int(input())
    arr = str_()
    s = ""
    s += arr[0]

    for i in range(1, n):
        a = s
        b = s

        a += arr[i]
        b = arr[i] + s

        if a > b:
            s = b
        else:
            s = a
            
    print(s)