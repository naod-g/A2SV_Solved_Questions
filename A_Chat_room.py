def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))


s = input().strip()

hello = "hello"
i = 0


for c in s:
    if i < 5 and c == hello[i]:
        i += 1

print("YES" if i == 5 else"NO")
