class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        cost = 0
        count_a = 0
        count_b = 0
        costs.sort(key = lambda x: abs(x[0]-x[1]), reverse = True)
        print(costs)

        for a, b in costs:
            if a <= b and count_a < n:
                cost += a
                count_a += 1
            elif a > b and count_b < n:
                cost += b
                count_b += 1
            else:
                if count_a == n:
                    cost += b
                if count_b == n:
                    cost += a

        return cost