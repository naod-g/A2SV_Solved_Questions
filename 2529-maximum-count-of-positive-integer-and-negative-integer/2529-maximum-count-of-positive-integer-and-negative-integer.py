class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # the last neg number
        l = 0
        r = len(nums)

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= 0:
                r = m - 1
            else:
                l = m + 1 
        neg = l

        # the first pos number
        l = 0
        r = len(nums)

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= 0:
                l = m + 1
            else:
                r = m - 1

        pos = len(nums) - l

        return max(neg, pos)
