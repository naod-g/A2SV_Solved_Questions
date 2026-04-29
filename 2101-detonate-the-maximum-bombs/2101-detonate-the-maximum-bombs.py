class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def bfs(i):
            visited = set()
            visited.add(i)
            q = deque([i])
            count = 1

            while q:
                a = q.popleft()
                x1, y1, r1 = bombs[a]

                for j in range(len(bombs)):
                    if j in visited:
                        continue
                    
                    x,y,r = bombs[j]
                    distance = sqrt(((x - x1)**2) + ((y - y1)**2))
                    
                    if distance <= r1:
                        count += 1
                        q.append(j)
                        visited.add(j)
         
            return count

        res = 0
        for i in range(len(bombs)):
            res = max(res, bfs(i))
        return res
