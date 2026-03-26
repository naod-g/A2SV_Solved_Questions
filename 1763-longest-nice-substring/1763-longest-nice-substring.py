class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def helper(s):
            if len(s) < 2:
                return ""
            
            sett = set(s)

            for i, ch in enumerate(s):

                if ch.swapcase() not in sett:
                    left = helper(s[0:i])
                    right = helper(s[i+1:])

                    return left if len(left) >= len(right) else right
            return s

        return helper(s)