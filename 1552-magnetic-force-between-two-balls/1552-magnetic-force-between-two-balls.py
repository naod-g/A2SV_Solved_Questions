class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def validator(val):
            pos = position[0]
            count = 1
            for i in range(1, len(position)):
                if position[i] - pos >= val:
                    count += 1
                    pos = position[i]
            if count >= m:
                return True

            return False

        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if validator(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans


            