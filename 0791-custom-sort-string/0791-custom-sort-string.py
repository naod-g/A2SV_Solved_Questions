class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return "".join(sorted(s, key = lambda ch: order.index(ch) if ch in order else len(order) ))

