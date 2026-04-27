class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        col = [-1] * len(graph)
        for i in range(len(graph)):
            if col[i] != -1:
                continue
            q = deque()
            q.append((i,0))

            while q:
                node, color = q.popleft()
                if col[node] == -1:
                    col[node] = color
                    for nei in graph[node]:
                        q.append((nei, color^1))
                if col[node] != color:
                    return False

        return True
