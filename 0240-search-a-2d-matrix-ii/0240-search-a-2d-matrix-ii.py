class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def merge(nums1, nums2):
            res = []
            i = j = 0

            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1

            res.extend(nums1[i:])
            res.extend(nums2[j:])
            return res

        flatten = matrix[0]
        for row in matrix[1:]:
            flatten = merge(flatten, row)

        i, j = 0, len(flatten)-1

        while i <= j:
            mid = (i+j) // 2
            if flatten[mid] == target:
                return True
            elif flatten[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return False




