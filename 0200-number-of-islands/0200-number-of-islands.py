class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0), (1,0), (0, 1), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        ans = 0

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col):
            if grid[row][col] == "1":
                grid[row][col] = "0"

                for a, b in directions:
                    nrow = row + a 
                    ncol = col + b
                    if inbound(nrow, ncol):
                        dfs(nrow, ncol)
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    dfs(row, col)
                    ans += 1

        return ans

    