class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flaten = []
        for row in matrix:
            flaten.extend(row)

        i = 0
        j = len(flaten) - 1

        while i <= j:
            mid = (i + j) // 2

            if flaten[mid] == target:
                return True
            elif flaten[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False