class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []


        def back(i):
            if i >= len(nums):
                res.add(tuple(curr[:]))
                return

            back(i+1)
            curr.append(nums[i])
            back(i+1)
            curr.pop()

        nums.sort()
        back(0)
        return list(res)