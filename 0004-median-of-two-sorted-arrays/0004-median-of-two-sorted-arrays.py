class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1
        nums3.extend(nums2)
        nums3.sort()

        n = len(nums3)
        print(nums3)

        if n%2:
            mid = n // 2
            return nums3[mid]
        else:
            mid2 = n // 2
            mid1 = mid2 - 1
            return (nums3[mid1] + nums3[mid2] ) / 2

