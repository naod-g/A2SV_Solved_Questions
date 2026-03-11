class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        a = SortedList()
        j = 0

        for i in range(len(nums)):
            a.add(nums[i])
            
            while len(a) > k:
                a.remove(nums[j])
                j += 1
            if i >= k-1:
                res.append(a[-1])

        return res
