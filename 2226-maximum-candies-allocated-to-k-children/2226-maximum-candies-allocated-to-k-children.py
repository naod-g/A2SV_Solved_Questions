class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        res = 0
        low = 1
        high = sum(candies) // k

        while low <= high:

            mid = (low + high) // 2

            count = 0
            for pile in candies:
                count += (pile//mid)

            if count >= k:
                res = max(res, mid)
                low = mid + 1
            else:
                high = mid -1

        return res
