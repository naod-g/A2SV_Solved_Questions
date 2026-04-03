class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def is_valid(capacity):
            day = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    day += 1
                    if day > days:
                        return False
            return True

        while left < right:
            mid = (left + right) // 2

            if is_valid(mid):
                right = mid
            else:
                left = mid + 1

        return right

