class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_count = len(matrix)
        col_count = len(matrix[0])

        zeros = []

        for i in range(row_count):
            for j in range(col_count):
                # 0 will be found at (i, j) and apppended in zeros
                if matrix[i][j] == 0:
                    zeros.append([i, j])
        
        for i, j in zeros:
            for a in range(col_count):
                matrix[i][a] = 0
                
            for b in range(row_count):
                matrix[b][j] = 0
        