class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def help(num, p):
            if p == 1:
                return num
            if p in memo:
                return memo[p]
            left, right = p // 2, ceil(p / 2)
            memo[p] = help(num, left) * help(num, right)
            return memo[p]
        if n < 0:
            ans = help(x, -n)
            return 1 / ans
        if n == 0:
            return 1
        return help(x, n)