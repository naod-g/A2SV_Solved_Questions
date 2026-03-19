class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2, -1, -1):
            prev = nums[i+1]
            curr = nums[i]


            if curr > prev:
                nums[i] = curr // ceil(curr / prev)
                count += ceil(curr / prev) - 1


        return count