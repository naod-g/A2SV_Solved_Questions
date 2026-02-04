class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ac_sum = n*(n+1) // 2
        nums_sum = sum(nums)
        return ac_sum - nums_sum

        
