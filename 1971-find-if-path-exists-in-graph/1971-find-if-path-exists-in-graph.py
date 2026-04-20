class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for v,u in edges:
            graph[v].append(u)
            graph[u].append(v)

        def dfs(node, visited):
            if node  == destination:
                return True
            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    if dfs(n, visited):
                        return True
                        
            return False

        return dfs(source, set())