class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0

        for house in houses:
            l = 0
            r = len(heaters) - 1
            min_radius = float("inf")

            while l <= r:
                mid = (l + r ) // 2

                if heaters[mid] > house:
                    r = mid - 1
                elif heaters[mid] < house:
                    l = mid + 1
                else:
                    min_radius = 0
                    break
                if abs(heaters[mid] - house) < min_radius:
                    min_radius = abs(heaters[mid] - house)
            res = max(res, min_radius)
        return res
                    