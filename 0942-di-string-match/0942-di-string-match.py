class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left = 0
        right = len(s)
        res = []

        for ch in s:
            if ch == 'I':
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1

        if s[-1] == 'I':
            res.append(left)
        else:
            res.append(right)


        return res