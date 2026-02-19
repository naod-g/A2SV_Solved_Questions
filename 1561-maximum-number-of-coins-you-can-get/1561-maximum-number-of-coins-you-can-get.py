class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort(reverse = True)
        i = 1

        for _ in range(len(piles)//3):
            res += piles[i]
            i += 2

        return res