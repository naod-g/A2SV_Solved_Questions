class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        max_sum = curr

        left = 0
        right = k
        while right < len(nums):
            print(curr)
            curr += nums[right]
            curr -= nums[left]
            
            max_sum = max(max_sum, curr)

            left += 1
            right += 1
        return max_sum / k