class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    break
                count += 1
        
        return (len(grid) * len(grid[0])) - count