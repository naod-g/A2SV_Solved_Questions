class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0] * len(s)
        mp = {}
        for i in range(0, 26):
            mp[i] = chr(i+97)
        
        for l, r, d in shifts:
            pre[l] += 1 if d == 1 else -1
            if r + 1 < len(s):
                pre[r+1] -= 1 if d == 1 else -1

        for i in range(1, len(s)):
            pre[i] += pre[i-1]
        
        res = []
        for i in range(len(s)):
            curr = (ord(s[i]) + pre[i]) - 97
            curr %= 26
            res.append(mp[curr])

            

        print(pre)
        print(res)
        return "".join(res)