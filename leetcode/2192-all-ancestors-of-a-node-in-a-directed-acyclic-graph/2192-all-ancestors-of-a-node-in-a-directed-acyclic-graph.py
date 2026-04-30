class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        indegree = [0]*n
        res = [set() for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # print(graph, indegree,res)
        q = deque([x for x in range(n) if indegree[x] == 0])

        while q:
            node = q.popleft()

            for nei in graph[node]:
                res[nei].add(node)
                res[nei].update(res[node])

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return [sorted(list(a)) for a in res] 
