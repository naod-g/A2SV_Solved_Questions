class Solution:
    def pancakeSort(self, nums: List[int]) -> List[int]:
        if nums == sorted(nums):
            return []

        n = len(nums) - 1 
        res = []
        sorted_nums = sorted(nums, reverse = True)

        for num in sorted_nums:
            idx = nums.index(num)
            res.append(idx+1)
            nums[:] = nums[idx::-1] + nums[idx+1:]

            res.append(n+1)
            if n < len(nums) - 1:
                nums[:] = nums[n::-1] + nums[n+1:]
            else:
                nums[:] = nums[n::-1]
            n -= 1

        return res[:-2]

        
