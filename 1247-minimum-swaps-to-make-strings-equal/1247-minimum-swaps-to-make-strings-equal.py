class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x' and s2[i] == 'y':
                    xy += 1
                else:
                    yx += 1
        if xy % 2 == yx % 2:
            return xy // 2 + yx // 2 + (xy % 2) * 2
        return -1