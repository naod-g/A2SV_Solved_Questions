class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diagonal = set()
        neg_diagonal = set()

        res = []
        board = [["."]*n for _ in range(n)]
        print(board)

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                col.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)

        backtrack(0)
        return res