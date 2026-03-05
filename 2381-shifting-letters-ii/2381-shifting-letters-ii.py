class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pre = [0] * n
        mp = {}
        for i in range(0, 26):
            mp[i] = chr(i+97)
        
        for l, r, d in shifts:
            pre[l] += 1 if d == 1 else -1
            if r + 1 < n:
                pre[r+1] -= 1 if d == 1 else -1

        for i in range(1, n):
            pre[i] += pre[i-1]
        
        res = [mp[((ord(s[i]) + pre[i]) - 97) % 26] for i in range(n)]

        return "".join(res)
