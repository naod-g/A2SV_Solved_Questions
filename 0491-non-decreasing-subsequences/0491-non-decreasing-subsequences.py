class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        def back(i):
            if i == len(nums):
                if len(curr) > 1 and curr not in res and curr == sorted(curr):
                    res.append(curr[:])
                return


            back(i+1)
            curr.append(nums[i])
            back(i+1)
            curr.pop()

        back(0)
        return res

