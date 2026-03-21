class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        even = ceil(n / 2)
        odd = n//2

        def pow(x, n):
            res = 1
            while n > 0:
                if n % 2:
                    res = (res * x) % MOD 
                n //= 2
                x = x ** 2 % MOD
            return res

        return pow(5, even) * pow(4, odd) % MOD