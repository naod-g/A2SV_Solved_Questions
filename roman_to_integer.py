class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500 ,
            "M": 1000
        }

        res = 0
        prev = 0

        for ch in reversed(s):
            val = mp[ch]
            if val >= prev:
                res += val
            else:
                res -= val
            prev = val
            
        return res
