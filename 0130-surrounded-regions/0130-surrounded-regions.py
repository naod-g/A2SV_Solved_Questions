class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1,0), (1,0), (0, 1), (0, -1)]
        n = len(board)
        m = len(board[0])
        visited = set()

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col):
            if board[row][col] == "O":
                visited.add((row, col))
                for a,b in directions:
                    nrow = row + a
                    ncol= col + b
                    if inbound(nrow, ncol) and (nrow, ncol) not in visited:
                        dfs(nrow, ncol)

        for row in range(n):
            for col in range(m):
                if row == 0 or row == n - 1 or col == 0 or col == m - 1:
                    dfs(row, col)

        for row in range(n):
            for col in range(m):
                if (row, col) not in visited:
                    board[row][col] = "X"

