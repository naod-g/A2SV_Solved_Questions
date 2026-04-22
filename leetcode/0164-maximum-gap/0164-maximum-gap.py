class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        mn = min(nums)
        buckets = defaultdict(list)

        for num in nums:
            if num == mx:
                idx = n-1
            else:
                idx = ((n-1)*(num - mn)) // (mx - mn)
            buckets[idx].append(num)

        pairs = []
        for i in range(n):
            if buckets[i]:
                pairs.append((min(buckets[i]), max(buckets[i])))

        ans = 0

        for i in range(1, len(pairs)):
            ans = max(ans, abs(pairs[i-1][1] - pairs[i][0]))

        return ans

        


        

