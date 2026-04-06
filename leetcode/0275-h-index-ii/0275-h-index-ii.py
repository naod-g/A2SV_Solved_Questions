class Solution:

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        for i in range(len(citations)):
            if citations[i] >= n - i:
                return n - i
                
        return 0