class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0]
        target = len(graph) - 1

        def dfs(node):
            if node == target:
                res.append(path[:])
                return

            for n in graph[node]:
                path.append(n)
                dfs(n)
                path.pop()
                
            

        dfs(0)
        return res

