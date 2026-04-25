class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = [0]*len(matrix)
        for i in range(len(matrix)):
            res[i] = sum(matrix[i])

        return res