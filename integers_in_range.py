class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        range_array = [0] * 51  # 1 to 50 inclusive

        for i, j in ranges:
            range_array[i - 1] += 1
            range_array[j] -= 1

        # prefix sum
        for i in range(1, 51):
            range_array[i] += range_array[i - 1]

        # check coverage
        for x in range(left - 1, right):
            if range_array[x] <= 0:
                return False

        return True
