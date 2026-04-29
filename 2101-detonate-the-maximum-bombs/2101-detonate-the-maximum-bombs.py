class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def bfs(i):
            visited = set()
            visited.add(i)
            q = deque([bombs[i]])
            count = 1

            while q:
                temp = q.popleft()
                for j in range(len(bombs)):
                    x,y,r = bombs[j]
                    if j in visited:
                        continue
                    
                    distance = sqrt(
                        ((x - temp[0])**2) + ((y - temp[1])**2)
                    )
                    
                    if distance <= temp[2]:
                        count += 1
                        q.append(bombs[j])
                        visited.add(j)
         
            return count

        res = 0
        for i in range(len(bombs)):
            res = max(res, bfs(i))
        return res
