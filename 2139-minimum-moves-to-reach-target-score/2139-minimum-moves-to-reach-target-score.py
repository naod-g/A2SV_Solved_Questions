class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0

        while target > 1:
            if maxDoubles == 0:
                break

            if target % 2 == 0:
                if maxDoubles:
                    target //= 2
                    maxDoubles -= 1
                else:
                    target -= 1
            elif target %2 == 1:
                target -= 1
            count += 1

        return count + (target - 1)
        


