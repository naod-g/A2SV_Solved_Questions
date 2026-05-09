def get_prime_factors(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors


class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        factors = get_prime_factors(n)

        for x in factors:
            if x not in[2,3,5]:
                return False
        return True