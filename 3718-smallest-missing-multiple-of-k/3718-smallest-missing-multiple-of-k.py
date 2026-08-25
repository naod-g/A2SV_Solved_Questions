class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        a = 1

        for i in range(k, mx+1, k):
            if i not in nums:
                return i
            a += 1
        return a * k