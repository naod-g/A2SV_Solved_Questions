class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        res = 0
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            res = max(right - left + 1, res)

        return res