class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pre = [nums[0]] * n
        moded = []
        mp = defaultdict(list)

        if len(nums) < 2:
            return False

        for i in range(1, n):
            pre[i] = (pre[i-1] + nums[i])

        for i in range(n):
            moded.append(pre[i] % k)

        for i, v in enumerate(moded):
            mp[v].append(i)

        for k, indexes in mp.items():
            if len(indexes) > 1:
                if indexes[-1] - indexes[0] >= 2:
                    return True

        for i in range(n):
            if moded[i] == 0 and i > 0:
                if pre[i] != 0:
                    return True
        for i in range(1, n):
            if moded[i] == 0:
                return True

        return False