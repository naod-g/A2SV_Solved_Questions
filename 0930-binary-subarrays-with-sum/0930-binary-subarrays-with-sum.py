class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        count = s = 0
        mp = Counter()
        
        for num in nums:
            s += num
            if s == goal:
                count += 1
            count += mp[s-goal]
            mp[s] += 1

        return count