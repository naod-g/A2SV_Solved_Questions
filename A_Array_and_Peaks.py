def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())

for _ in range(t):
    n, k = list_()

    if k == 0:
        res = [x for x in range(1, n+1)]

    elif n == 1 or n == 2: # this is also k > 0
        res = [-1]

    else:   # n > 2
        res = []

        nums = [num+1 for num in range(n)]

        peeks = n//2 if n % 2 == 1 else (n//2)-1
        peek_ptr = n - k

        if k > peeks:
            res.append(-1)

        else:
            for i in range(n-k):
                res.append(nums[i])
                if peek_ptr < n:
                    res.append(nums[peek_ptr])
                    peek_ptr += 1

    print(" ".join([str(num) for num in res]))

