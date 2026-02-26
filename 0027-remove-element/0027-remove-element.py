class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        placeh = 0

        for seek in range(len(nums)):
            if nums[seek] != val:
                nums[seek], nums[placeh] = nums[placeh], nums[seek]
                placeh += 1
                
        return placeh
        
