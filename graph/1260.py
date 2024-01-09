#DFS와 BFS(실버 2)

from collections import deque
#DFS
def dfs(x):
  print(x, end=' ')

  for t in graph[x]:
    if not visited_dfs[t]:
      visited_dfs[t] = True
      dfs(t)

#BFS
def bfs(x):
  visited_bfs = [False] * (n + 1)
  queue = deque()
  queue.append(x)
  visited_bfs[x] = True
  print(x, end = ' ')
  while queue:
    now = queue.popleft()
    for t in graph[now]:
      if not visited_bfs[t]:
        visited_bfs[t] = True
        queue.append(t)
        print(t, end = ' ')
      
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n + 1):
  graph[i].sort()

visited_dfs = [False] * (n + 1)
visited_dfs[v] = True
dfs(v)
print()
bfs(v)