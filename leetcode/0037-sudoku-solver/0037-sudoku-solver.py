class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i//3, j//3)].add(board[i][j])
        
        def back(i,j):
            if i >= 9:
                return True
            if j >= 9:
                return back(i+1, 0)

            if board[i][j] != ".":
                return back(i, j+1)

            for k in range(1, 10):
                a = str(k)
                if a not in row[i] and a not in col[j] and a not in box[(i//3, j//3)]:
                    board[i][j] = a
                    row[i].add(a)
                    col[j].add(a)
                    box[(i//3, j//3)].add(a)

                    if back(i,j+1):
                        return True
                    
                    board[i][j] = "."
                    row[i].remove(a)
                    col[j].remove(a)
                    box[(i//3, j//3)].remove(a)
            return False

        back(0,0)



                
