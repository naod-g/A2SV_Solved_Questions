class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seek = 0
        placeholder = 0

        while seek < len(nums) and placeholder < len(nums):
            if nums[seek] != 0:
                nums[seek], nums[placeholder] = nums[placeholder], nums[seek]
                placeholder += 1
            seek += 1
        