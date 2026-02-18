class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sorted_nums = sorted(nums)

        for num in nums:
            res.append(sorted_nums.index(num))

        return res
        

        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             count += 1
        #     res.append(count)

        # return res
