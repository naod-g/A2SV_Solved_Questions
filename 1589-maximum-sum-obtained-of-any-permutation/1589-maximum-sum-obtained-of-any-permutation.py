class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pre = [0] * n
        count = 0

        for a,b in requests:
            pre[a] += 1
            if b+1 < n:
                pre[b+1] -= 1

        for i in range(1, n):
            pre[i] += pre[i-1]

        pre.sort()
        nums.sort()

        for i in range(n):
            count += nums[i] * pre[i]

        return count % (10**9 + 7)