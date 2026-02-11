class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majority = 0
        count = 0

        for num in nums:
            if count == 0:
                majority = num
                count += 1
            elif majority == num:
                count += 1
            else:
                count -= 1

        left = 0
        right = nums.count(majority)
        leftlen = 0
        rightlen = len(nums)

        for i in range(len(nums)):
            if nums[i] == majority:
                left += 1
                right -= 1
            leftlen += 1
            rightlen -= 1

            if right * 2 > rightlen and left * 2 > leftlen:
                return i
        return -1
