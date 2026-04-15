class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = set()

        for i in range(len(nums)):
            while nums[i] != i+1:
                j = nums[i] - 1

                if nums[i] == nums[j]:
                    res.add(nums[i])
                    break
                else:   
                    nums[i], nums[j] = nums[j], nums[i]

        res2 = set()
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                res2.add(i+1)

            i += 1

        return list(res) + list(res2)

