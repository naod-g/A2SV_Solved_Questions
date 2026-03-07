class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        mp = {0:1}

        pre = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] + nums[i]
        
        for num in pre:
            remainder = num % k
            if remainder in mp:
                count += mp[remainder]
                mp[remainder] += 1
            else:
                mp[remainder] = 1

        return count