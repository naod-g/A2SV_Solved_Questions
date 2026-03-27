class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        n = len(nums)

        def backtracking(i):
            if i >= len(nums):
                res.append(curr[:])
                return 

            backtracking(i+1)

            curr.append(nums[i])
            backtracking(i+1)
            curr.pop()

        backtracking(0)
        return res