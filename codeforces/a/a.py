from collections import deque

def list_(): return list(map(int, input().split()))
def str_(): return list(map(str, input().split()))

t = int(input())
graph = [[] for i in range(t+1)]

for _ in range(t-1):
    u, v = list_()
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    dist = [-1] * (t + 1)
    q = deque([start])
    dist[start] = 0
    far = start

    while q:
        node = q.popleft()
        for nei in graph[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                q.append(nei)
                if dist[nei] > dist[far]:
                    far = nei

    return far, dist[far]

a, _ = bfs(1)
b, d = bfs(a)

print(d * 3)