class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[]* n for _ in range(n)]
        degree = [0]*n

        for u,v in prerequisites:
            graph[v].append(u)
            degree[u] += 1

        q = deque()
        res = []

        for i in range(n):
            if degree[i] == 0:
                q.append(i)

        while q:
            c = q.popleft()
            res.append(c)

            for nei in graph[c]:
                degree[nei] -= 1

                if degree[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == n else []


