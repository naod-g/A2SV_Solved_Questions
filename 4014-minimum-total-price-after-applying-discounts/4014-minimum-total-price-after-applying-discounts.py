class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        total = 0
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        i = 0

        for d in discounts:
            if i <len(prices):
                total += (prices[i] * (100 - d)) / 100
                i+=1
        total += sum(prices[i:])
        return total

