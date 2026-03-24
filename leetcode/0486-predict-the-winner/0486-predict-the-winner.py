class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def func(i, j, turn):
            if i == j:
                return nums[j]
            if turn:
                return max(nums[i] + func(i+1,j, not turn), nums[j] + func(i,j-1, not turn))
            return min(-nums[i] + func(i+1,j, not turn), -nums[j] + func(i,j-1, not turn))

        return func(0, len(nums)-1, True) >= 0
            
