class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [nums[0]] * n

        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i]
            
        mn = min(pre)
        return abs(mn) + 1 if mn <= 0 else 1