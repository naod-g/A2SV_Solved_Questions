class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0

        for i in range(len(nums)):
            curr = max(curr-1, nums[i])

            if curr <= 0 and i != len(nums)- 1:
                return False
            

        return True