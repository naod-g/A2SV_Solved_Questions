class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, curr = [], []

        def back(i):
            if i > n:
                if len(curr) == k:
                    res.append(curr[:])
                return
            back(i+1)

            curr.append(i)
            back(i+1)
            curr.pop()

        back(1)
        return res