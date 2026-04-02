class Solution:
    def nearest(self, heaters, house):
            left = 0
            right = len(heaters)

            while left < right:
                mid = (right + left ) // 2
                if heaters[mid] < house:
                    left = mid + 1
                elif heaters[mid] < house:
                    right = mid + 1
                else:
                    right = mid

                i = left  # insertion index

            left_dist = float('inf')
            if i > 0:
                left_dist = house - heaters[i-1]

            right_dist = float('inf')
            if i < len(heaters):
                right_dist = heaters[i] - house

            return min(left_dist, right_dist)

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses:
            distance = self.nearest(heaters, house)
            ans = max(distance, ans)
        return ans