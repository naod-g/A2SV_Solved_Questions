class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [list(row)[::-1] for row in list(zip(*matrix))]

        # list(zip(*matrix)) = Transpose 
        # list(row)[::-1] = reverse the transposed and chnaged it to list instead of tuple
        