class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            sm[i] = sm[i-1] + nums[i]

        return sm