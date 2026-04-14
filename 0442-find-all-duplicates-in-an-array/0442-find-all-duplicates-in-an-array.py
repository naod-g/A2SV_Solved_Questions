class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = []

        for i in range(len(nums)):
            while nums[i] != i+1:
                j = nums[i] - 1

                if nums[i] == nums[j]:
                    arr.append(nums[i])
                    break
                else:   
                    nums[i], nums[j] = nums[j], nums[i]

        return list(set(arr))
