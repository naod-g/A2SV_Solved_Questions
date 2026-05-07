class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = [x for row in matrix for x in row]
        return sorted(nums)[k-1]