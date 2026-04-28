class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        direction = [(-1,0), (1,0), (0, -1), (0,1)]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col <len(grid[0])

        def dfs(row, col, prow, pcol, color):
            visited.add((row, col))

            for a,b in direction:
                nr = row + a
                nc = col + b

                if nr == prow and nc == pcol:
                    continue

                if inbound(nr, nc) and (nr,nc) not in visited and grid[nr][nc] == color:
                    if dfs(nr, nc, row, col, color):
                        return True
                    continue
                elif inbound(nr, nc) and grid[nr][nc] == color:
                    return True

            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    if dfs(i,j,-1,-1,grid[i][j]):
                        return True
        return False

        






