class Solution:
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m1 = self.rotator(mat)
        m2 = self.rotator(m1)
        m3 = self.rotator(m2)

        if mat == target or target == m1 or target == m2 or target == m3:
            return True
        return False

            

    def rotator(self, matrix):
        res = [[1] * len(matrix) for row in matrix]

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix)):
                res[i][j] = matrix[j][i]

        res[:] = [row[::-1] for row in res]

        return res
