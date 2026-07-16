class Solution:
    
    def maxDigitRange(self, nums: list[int]) -> int:
        def rang(x):
            mn = min([int(num) for num in str(x)])
            mx = max([int(num) for num in str(x)])
            return mx - mn

        mp = [(num, rang(num)) for num in nums]
        total = 0
        mx = 0
        
        for x in mp:
            if x[1] > mx:
                mx = x[1]

        for x in mp:
            if x[1] == mx:
                total += x[0]

        return total

 

