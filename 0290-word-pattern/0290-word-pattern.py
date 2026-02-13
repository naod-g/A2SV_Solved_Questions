class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # return len(set(pattern)) == len(set(s.split()))
        words = s.split()
        mp = {}
        count1 = Counter(pattern)
        count2 = Counter(words)

        pairs = set(zip(count1, count2))
        print(pairs)

        for p, s in pairs:
            if count1[p] != count2[s]:
                return False

        for word in words:
            if not any(word in t for t in pairs):
                return False
        if len(pattern) != len(words):
            return False

        i = 0
        for letter in pattern:
            if letter not in mp:
                mp[letter] = words[i]
            elif mp[letter] != words[i]:
                return False
            i += 1

        return True
