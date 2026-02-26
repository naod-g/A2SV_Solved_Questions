class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p = 0

        for s in range(len(nums)):
            if nums[s] %2 == 0:
                nums[p], nums[s] = nums[s], nums[p]
                p += 1
                
        return nums