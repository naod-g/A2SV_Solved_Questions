class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  
        mx = 0

        for num in num_set:
            curr = num
            if curr - 1 not in num_set:
                count = 1
                
                while curr + 1 in num_set:
                    curr += 1
                    count += 1
                mx = max(mx, count)

        return mx

