class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        curr_line = []
        inblock = False

        for line in source:
            i = 0
            if not inblock:
                curr_line = []
            while i < len(line):
                #single line comments
                if not inblock and i+1 < len(line) and line[i] == "/" and line[i+1] == "/":
                    # if curr_line:
                    #     res.append("".join(curr_line))
                    break

                # start of multiline comments
                elif not inblock and i+1 < len(line) and line[i] == "/" and line[i+1] == "*":
                    inblock = True
                    i += 2

                # end of multiline comment
                elif inblock and line[i] == "*" and line[i+1] == "/":
                    inblock = False
                    i += 2
                # normal code
                elif not inblock:
                    curr_line.append(line[i])
                    i += 1

                # inside block comment: skip
                else:
                    i += 1
            if curr_line and not inblock:
                res.append("".join(curr_line))
            

        return res
