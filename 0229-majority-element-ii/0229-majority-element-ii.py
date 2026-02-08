class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cand1, cand2 = None, None
        count1, count2 = 0, 0


        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 += 1
            elif count2 == 0:
                cand2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        return [c for c in [cand1, cand2] if nums.count(c) > (n//3) ]
