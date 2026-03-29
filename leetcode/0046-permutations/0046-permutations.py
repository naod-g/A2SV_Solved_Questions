class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        def back():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    back()
                    curr.pop()

        back()
        return res
