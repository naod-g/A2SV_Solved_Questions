class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            if node == destination:
                return True

            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    found = dfs(n, visited)
                    if found:
                        return True
            return False

        return dfs(source, set())