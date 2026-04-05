class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = [0, 0]
        mp = {"L": [-1, 0], 
                "R": [1, 0], 
                "U": [0, 1], 
                "D": [0, -1] }

        for move in moves:
            origin[0] += mp[move][0]
            origin[1] += mp[move][1]

        return origin == [0, 0]