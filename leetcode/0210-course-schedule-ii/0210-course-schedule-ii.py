class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[]*n for _ in range(n)]
        indegree = [0]*n

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        # print(graph,indegree)
        res = []
        q = deque([x for x in range(n) if indegree[x] == 0])

        while q:
            course = q.pop()
            res.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return res if len(res) == n else []