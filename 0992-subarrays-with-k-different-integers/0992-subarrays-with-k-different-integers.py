class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.func(nums, k) - self.func(nums, k-1)

    def func(self, nums: List[int], k: int):
        window = defaultdict(int)
        left = 0
        count = 0

        for right in range(len(nums)):
            window[nums[right]] += 1

            while len(window) > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]

                left += 1
            count += right - left + 1

        return count