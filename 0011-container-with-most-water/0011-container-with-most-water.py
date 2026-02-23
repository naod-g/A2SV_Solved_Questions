class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_container = 0
        current_container = 0

        while i < j:
            current_container = min(height[i], height[j]) * (j - i)
            max_container = max(max_container, current_container) 
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1   
        return max_container 
            
        