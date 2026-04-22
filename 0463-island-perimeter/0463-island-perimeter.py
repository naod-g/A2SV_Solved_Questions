class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        direction = [(-1,0), (0,1), (1,0), (0, -1)]

        def dfs(i, j):

            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            
            if (i,j) in visited:
                return 0

            visited.add((i,j))
            p = 0
            for d in direction:
                p += dfs(i+d[0], j+d[1])
            return p

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                   return dfs(i, j)
        
            

