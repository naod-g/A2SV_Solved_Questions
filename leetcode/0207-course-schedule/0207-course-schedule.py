class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = [[]*n for i in range(n)]
        indegree = [0]*n
        res = []

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([x for x in range(n) if indegree[x] == 0])

        while q:
            course = q.pop()
            res.append(course)
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return len(res) == n
