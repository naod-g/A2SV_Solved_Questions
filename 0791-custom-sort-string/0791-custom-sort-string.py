class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        count = Counter(s)

        for ch in order:
            if ch in s:
                res.append(ch * count[ch])

        res = "".join(res)
        for ch in s:
            if ch not in res:
                res += (ch * count[ch])

        return res
