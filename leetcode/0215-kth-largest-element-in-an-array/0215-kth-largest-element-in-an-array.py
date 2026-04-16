class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)

        arr = [0] * (mx - mn + 1)

        for num in nums:
            arr[num-mn] += 1

        remain = k
        for i in range(len(arr)-1, -1, -1):
            remain -= arr[i]

            if remain <= 0:
                return i + mn

            