class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        roots = []
        lines = []
        res = []

        for path in paths:
            line = path.split()
            roots.append(line[0])
            lines.append(line[1:])


        new_roots = [r for r, files in zip(roots, lines) for _ in files]
        new_lines = [f for files in lines for f in files]


        n = len(new_lines)

        file_no =  [ch.split(".")[0] for ch in new_lines]
        file_ext = [ch[ch.find(".")+1 : ch.find("(")] for ch in new_lines]
        content =  [ch[ch.find("(")+1 : ch.find(")")] for ch in new_lines]

        visited = set()
        for i in range(n):
            if content[i] in visited:
                continue
            
            visited.add(content[i])
            temp = [f"{new_roots[i]}/{file_no[i]}.{file_ext[i]}"]

            for j in range(i + 1, n):
                if content[i] == content[j] and content[j]:
                    temp.append(f"{new_roots[j]}/{file_no[j]}.{file_ext[j]}")
                    
            if len(temp) > 1:
                res.append(temp)

        return res