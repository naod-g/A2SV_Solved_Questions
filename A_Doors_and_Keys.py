t = int(input())

for _ in range(t):
    s = str(input())
    mp = {s[i]: i for i in range(6)}
    
    res = "YES"
    if mp['r'] > mp['R']:
        res = "NO"
    if mp['b'] > mp['B']:
        res = "NO"
    if mp['g'] > mp['G']:
        res = "NO"
    
    print(res)

