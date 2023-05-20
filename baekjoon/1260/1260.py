from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i].sort()
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

def dfs(now):
    dfs_visited[now] = True
    print(now, end = " ")
    for next in graph[now]:
        if not dfs_visited[next]:
            dfs(next)

def bfs(x):
    queue = deque([x])
    bfs_visited[x] = True
    while queue:
        now = queue.popleft()
        print(now, end = " ")
        for next in graph[now]:
            if not bfs_visited[next]:
                queue.append(next)
                bfs_visited[next] = True

dfs(v)
print()
bfs(v)