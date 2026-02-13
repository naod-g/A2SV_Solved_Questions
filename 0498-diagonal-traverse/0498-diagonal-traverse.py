class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_count = len(mat)
        col_count = len(mat[0])

        res = []

        is_up = True
        row, col = 0, 0

        for i in range(row_count * col_count):
            # going up diagonal
            if is_up:
                res.append(mat[row][col])
                row -= 1
                col += 1

                if col >= col_count:
                    row += 2
                    col -= 1
                    is_up = False

                elif row < 0:
                    row = 0
                    is_up = False

            # going down diagonal
            else: 
                res.append(mat[row][col])
                row += 1
                col -= 1

                if row >= row_count:
                    col += 2
                    row -= 1
                    is_up = True

                if col < 0:
                    col = 0
                    is_up = True
                
        return res
    