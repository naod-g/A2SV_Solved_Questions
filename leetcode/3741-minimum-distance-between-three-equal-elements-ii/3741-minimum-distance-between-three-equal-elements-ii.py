class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float("inf")
        mp = defaultdict(list)
        for i in range(len(nums)):
            mp[nums[i]].append(i)

        for k,v in mp.items():
            if len(v) >= 3:
                for i in range(2,len(v)):
                    mx = max(v[i-2], v[i-1], v[i])
                    mn = min(v[i-2], v[i-1], v[i])
                    res = min(res, 2*(mx-mn))

        return res if res != float("inf") else -1


                    
            