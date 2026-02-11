class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # operation 1
        if set(word1) != set(word2):
            return False

        # operation 2
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True
