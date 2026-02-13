class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_count = len(img)
        col_count = len(img[0])
        res = [[0] * col_count for i in range(row_count)]

        directions = [  (-1,-1), (-1,0), (-1,1),
                        (0, -1), (0, 0), (0, 1),
                        (1, -1), (1, 0), (1, 1) ]

        for row in range(row_count):
            for col in range(col_count):
                total = 0
                count = 0
                for dr, dc in directions: 
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < row_count and 0 <= nc < col_count:
                        total += img[nr][nc]
                        count += 1
                        
                res[row][col] = total // count
                

        return res
