class Solution:
    def minRotations(self, s: str) -> int:
        count = 0
        p = 0
        for num in s:
            curr = int(num)
            clk = abs(p-curr)
            count += min(clk, 10-clk)
            p = curr

        return count

