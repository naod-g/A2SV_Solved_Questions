class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []


        def back(i):
            if i >= len(nums):
                if sorted(curr) not in res:
                    res.append(sorted(curr[:]))
                return

            back(i+1)

            curr.append(nums[i])
            back(i+1)
            curr.pop()

        back(0)
        return res