class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            s = str(num)
            for i in range(len(s)):
                res.append(int(s[i]))

        return res
