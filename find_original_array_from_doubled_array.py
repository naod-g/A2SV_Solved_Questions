class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        freq = Counter(changed)
        res = []

        if n%2 != 0:
            return res

        for num in sorted(changed):
            if freq[num] == 0: # double of prev number
                continue
            if freq[num*2] == 0: # also using the doubled number
                return []

            res.append(num)
            freq[num] -= 1
            freq[num*2] -= 1

        return res

        
