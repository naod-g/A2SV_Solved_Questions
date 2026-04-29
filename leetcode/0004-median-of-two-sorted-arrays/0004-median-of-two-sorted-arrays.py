class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        o = len(nums1)
        if o % 2 == 0:
            return (nums1[o // 2 - 1] + nums1[o // 2]) / 2
        if o % 2 != 0:
            return nums1[o // 2]