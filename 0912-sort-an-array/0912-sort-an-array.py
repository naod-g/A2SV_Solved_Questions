class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergearray(i,j,nums):
            if i == j:
                return [nums[i]]

            mid = (i + j) // 2
            left = mergearray(i, mid, nums)
            right = mergearray(mid+1, j, nums)

            return merge(left, right)

        def merge(left, right):
            i = 0
            j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])

            return res

        return mergearray(0, len(nums)- 1, nums)





