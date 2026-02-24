class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        ends = []
        revs = s[::-1]

        for ch in set(s):
            ends.append([s.index(ch), len(s) - revs.index(ch) - 1])
        ends.sort()


        start, end = ends[0]
        for left, right in ends[1:]:
            if start <= left <= end:
                end = max(end, right)
            else:
                res.append(end - start + 1)
                start = left
                end = right
        res.append(end - start + 1)
        return res
        


            
