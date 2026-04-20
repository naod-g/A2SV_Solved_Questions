class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mp = Counter(nums)

        nums[:mp[0]] = [0] * mp[0]
        nums[mp[0]:mp[0]+mp[1]] = [1] * mp[1]
        nums[mp[0]+mp[1]:] = [2] * mp[2]
