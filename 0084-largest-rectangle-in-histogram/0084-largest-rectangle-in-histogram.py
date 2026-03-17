class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx,height = stack.pop()

                if height * (i - idx) > res:
                    res = height * (i - idx)
                start = idx

            stack.append((start, h))

        for i,h in stack:
            if h * (n - i) > res:
                res = h * (n - i)

        return res

        