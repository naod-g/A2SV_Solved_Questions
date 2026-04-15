class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            while nums[i] != i+1:
                j = nums[i] - 1

                if nums[i] == nums[j]:
                    res.append(nums[i])
                    break
                else:   
                    nums[i], nums[j] = nums[j], nums[i]

        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                res.append(i+1)

            i += 1

        return res

