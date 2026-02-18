class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                a = "".join([str(nums[j]), str(nums[j+1])])
                b = "".join([str(nums[j+1]), str(nums[j])])
                if a < b:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        s = [str(num) for num in nums]
        if s.count("0") == len(s):
            return "0"
        return "".join(s)