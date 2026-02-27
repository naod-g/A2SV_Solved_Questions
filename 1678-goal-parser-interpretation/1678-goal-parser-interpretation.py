class Solution:
    def interpret(self, command: str) -> str:
        res = []
        for i in range(1, len(command)):
            if command[i-1] == "G":
                res.append("G")
            if command[i-1] == "(" and command[i] == ")":
                res.append("o")
            if command[i-1] == "(" and command[i] == "a":
                res.append("al")
        res.append("G" if command[-1] == "G" else "")

        return "".join(res)
