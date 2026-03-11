class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = deque()

        left = 0
        for right in range(len(nums)):
            while d and nums[d[-1]] < nums[right]:
                d.pop()
            d.append(right)

            if left > d[0]:
                d.popleft()
                
            
            if right + 1 >= k:
                res.append(nums[d[0]])
                left += 1

        return res