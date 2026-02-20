class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return "".join(sorted(s, key = lambda ch: order.index(ch) if ch in order else len(order) ))

        # res = []
        # count = Counter(s)

        # for ch in order:
        #     if ch in s:
        #         res.append(ch * count[ch])

        # res = "".join(res)
        # for ch in s:
        #     if ch not in res:
        #         res += (ch * count[ch])

        # return res
