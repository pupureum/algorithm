from sys import stdin

n = int(stdin.readline().rstrip())
a, b = map(int, stdin.readline().split())
m = int(stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    q, w = map(int, stdin.readline().split())
    graph[q].append(w)
    graph[w].append(q)
visited = [False] * (n + 1)
result = []

def dfs(now, count):
    count += 1
    visited[now] = True
    if now == b:
        result.append(count)
    for next in graph[now]:
        if not visited[next]:
            dfs(next,count)

dfs(a,0)
if len(result) != 0:
    print(result[0]-1)
else:
    print(-1)