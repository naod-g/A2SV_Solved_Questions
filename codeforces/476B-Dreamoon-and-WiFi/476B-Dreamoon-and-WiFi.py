from collections import Counter

s1 = input()
s2 = input()

mp1 = Counter(s1)
mp2 = Counter(s2)
total = 2 ** mp2['?']

res = []
curr = []
n = len(s2)
count = 0

def back(i, curr):
    global count
    if i == n:
        # res.append("".join(curr))
        temp = Counter(curr)
        if temp['+'] == mp1['+'] and temp['-'] == mp1['-']:
            count += 1
        return
    
    if s2[i] == "?":
        curr.append('+')
        back(i+1, curr)
        curr.pop()

        curr.append('-')
        back(i+1, curr)
        curr.pop()

    else:
        curr.append(s2[i])
        back(i+1, curr)
        curr.pop()

back(0, [])
print(count/total)