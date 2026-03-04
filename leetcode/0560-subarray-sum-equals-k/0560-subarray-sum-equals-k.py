class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] + nums[i]

        freq = Counter()
        for num in pre:
            if num == k:
                count += 1
            count += freq[num - k]
            freq[num] += 1
        return count