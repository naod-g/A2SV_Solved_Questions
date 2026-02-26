class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        left = 0
        sm = 0

        for right in range(len(nums)):
            sm += nums[right]

            while sm >= target:
                ans = min(ans, right - left + 1)
                sm -= nums[left]
                left += 1

                
        return ans if ans != float("inf") else 0