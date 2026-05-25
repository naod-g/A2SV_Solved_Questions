class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        mp = Counter(nums)
        for key,v in mp.items():
            if v > k:
                mp[key] = k
        # print(mp)
        for key,v in mp.items():
            res.extend([key]*v)
        return sorted(res)
