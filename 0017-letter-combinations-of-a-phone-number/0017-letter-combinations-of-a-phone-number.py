class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, curr = [], []

        mp = {}
        a = 95
        for i in range(2, 10):
            if i == 7 or i == 9:
                mp[str(i)] = [chr(a+i), chr(a+i+1), chr(a+i+2), chr(a+i+3)]
                a += 3
            else:
                mp[str(i)] = [chr(a+i), chr(a+i+1), chr(a+i+2)]
                a += 2

        def back(i):
            if i == len(digits):
                if len(curr) == len(digits):
                    res.append("".join(curr[:]))
                return
            for ch in mp[digits[i]]:
                curr.append(ch)
                back(i+1)
                curr.pop()

        back(0)
        return res