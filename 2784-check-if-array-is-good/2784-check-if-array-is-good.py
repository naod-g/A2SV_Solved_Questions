class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mp = Counter(nums)
        mx = max(nums)
        if mp[mx] != 2:
            return False 

        for num in range(1, mx+1):
            if num != mx and mp[num] != 1:
                return False
        
        return True

