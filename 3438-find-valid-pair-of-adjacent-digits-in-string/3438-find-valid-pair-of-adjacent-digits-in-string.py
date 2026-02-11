class Solution:
    def findValidPair(self, s: str) -> str:
        mp = Counter(s)

        if len(s) <= 2:
            return ""

        for i in range(len(s)-1):
            a, b = int(s[i]), int(s[i+1])
            print(a,b)

            if a != b:
                if mp[str(a)] == a and mp[str(b)] == b:
                    return "".join([str(a),str(b)])

        return ""
