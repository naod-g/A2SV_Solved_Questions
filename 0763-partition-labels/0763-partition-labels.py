class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        mp = defaultdict(int)
        for i, ch in enumerate(s):
            mp[ch] = i

        i = 0
        while i < len(s):
            start = i
            right = mp[s[start]]

            while i < right:
                right = max(right, mp[s[i]])
                i += 1
            res.append(right - start + 1)
            i += 1
            
        return res
            
            
