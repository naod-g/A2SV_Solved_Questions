class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def bfs(i):
            visited = set()
            visited.add(i)
            q = deque([bombs[i]])
            count = 1

            while q:
                x1, y1, r1 = q.popleft()

                for j in range(len(bombs)):
                    if j in visited:
                        continue
                    
                    x,y,r = bombs[j]
                    distance = sqrt(((x - x1)**2) + ((y - y1)**2))
                    
                    if distance <= r1:
                        count += 1
                        q.append(bombs[j])
                        visited.add(j)
         
            return count

        res = 0
        for i in range(len(bombs)):
            res = max(res, bfs(i))
        return res
