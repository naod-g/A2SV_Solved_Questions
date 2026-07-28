def yn(num):
    s = [int(i) for i in str(num)]
    for digit in s:
        if digit == 0 or num % digit != 0:
            return False
    return True

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            if yn(num):
                res.append(num)

        return res