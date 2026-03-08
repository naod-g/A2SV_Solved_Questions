class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(num for num in nums)


        for i in range(2 ** n):
            curr = list(bin(i)[2:])
            while len(curr) < n:
                curr.insert(0, "0")
            curr = "".join(curr)

            if curr not in nums:
                return curr


        

        