class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        a = 0
        for x in nums:
            if x%2 == 0:
                a += x

        for val, idx in queries:
            if nums[idx] %2 == 0:
                a -= nums[idx]

            nums[idx] += val

            if nums[idx] %2 == 0:
                a += nums[idx]

            res.append(a)
        return res