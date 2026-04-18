class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        res = []

        if sides[0] + sides[1] > sides[2]:
            x,y,z = sides
            a = (x**2 + y**2 - z**2) / (2 * x * y)
            b = (x**2 + z**2 - y**2) / (2 * x * z)
            c = (y**2 + z**2 - x**2) / (2 * y * z)

            res.append(degrees(acos(a)))
            res.append(degrees(acos(b)))
            res.append(degrees(acos(c)))
            res.sort()

        return res    