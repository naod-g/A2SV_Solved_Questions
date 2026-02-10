class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        rowb = colb = 0
        rowe, cole= n-1, m-1

        is_right = is_left = is_down = False
        is_up = True

        res = []

        while rowb <= rowe and colb <= colb:
            # going right
            if is_up:
                for i in range(rowb, cole+1):
                    res.append(matrix[rowb][i])
                    is_right = True
                    is_left = is_up = is_down = False
                rowb += 1

            # going down
            if is_right:
                for i in range(rowb, rowe+1):
                    res.append(matrix[i][cole])
                    is_down = True
                    is_left = is_up = is_right = False
                cole -= 1

            # going left
            if is_down:
                for i in range(cole, colb-1, -1):
                    res.append(matrix[rowe][i])
                    is_left = True
                    is_right = is_up = is_down = False
                rowe -= 1

            # going up
            if is_left:
                for i in range(rowe, rowb-1, -1):
                    res.append(matrix[i][colb])
                    is_up = True
                    is_left = is_right = is_down = False
                colb += 1
        
        return res
            



