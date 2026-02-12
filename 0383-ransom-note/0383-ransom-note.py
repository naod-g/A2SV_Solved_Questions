class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = Counter(magazine)

        for ch in ransomNote:
            if mp[ch] > 0:
                mp[ch] -= 1
            elif mp[ch] == 0:
                return False

        return True