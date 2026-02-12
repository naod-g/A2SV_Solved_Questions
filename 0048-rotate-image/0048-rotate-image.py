class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # this is transposed but in tuple format "list(zip(*matrix))"
        res = [list(row)[::-1] for row in list(zip(*matrix))]
        matrix[:] = res
        