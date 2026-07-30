class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        elif n <= 16:
            return 8 + 2*(n-8)
        elif n <= 24:
            return 24 + 3*(n-16)
        else:
            return 8 + 16 + 24 + 4*(n-24)