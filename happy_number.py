class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            new_num = 0
            visited.add(n)

            for digit in str(n):
                new_num += (int(digit) ** 2)

            if new_num in visited:
                break
            n = new_num

        return new_num == 1
