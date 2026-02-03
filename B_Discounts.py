def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


n = int(input())


for i in range(n):
    price = 0
    current = 0
    p, v = list_()
    prices = list_()
    discounts = list_()

    prices.sort(reverse = True)
    discounts.sort()

    i = 0
    j = 0

    while i < p and j < v:
        if discounts[j] == 1:
            i += 1
        else:
            current = prices[i: discounts[j]-1 + i]
            price += sum(current)

            i += discounts[j]

        j += 1
    price += sum(prices[i:])
    print(price)

    print("n"+4)
        