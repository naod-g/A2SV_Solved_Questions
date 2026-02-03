def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

s = str(input()).lower()
t = str(input()).lower()

for i in range(len(s)):
    if s[i] == t[i]:
        continue
    elif s[i] > t[i]:
        print(1)
        break
    elif s[i] < t[i]:
        print(-1)
        break
else:
    print(0)