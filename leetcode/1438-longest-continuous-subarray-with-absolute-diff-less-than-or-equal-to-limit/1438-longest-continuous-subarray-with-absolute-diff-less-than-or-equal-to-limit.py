class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        imono = deque()
        dmono = deque()
        left = 0

        for right in range(len(nums)):
            while imono and nums[right] > imono[-1]:
                imono.pop()
            while dmono and nums[right] < dmono[-1]:
                dmono.pop()

            imono.append(nums[right])
            dmono.append(nums[right])

            if imono[0] - dmono[0] > limit:
                if imono[0] == nums[left]:
                    imono.popleft()
                if dmono[0] == nums[left]:
                    dmono.popleft()
                left += 1

        return len(nums) - left