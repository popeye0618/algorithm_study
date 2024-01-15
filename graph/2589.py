#보물섬(골드 5)
#내 풀이
#육지마다 bfs를 돌려서 가장 먼 곳을 찾는다.

from collections import deque

def bfs(x, y):
  global max_value
  visited = [[0 for _ in range(m)] for _ in range(n)]
  
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 'L':
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))
  
  nmax = max(max(x) for x in visited)
  max_value = max(max_value, nmax)

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_value = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'L':
      bfs(i, j)

print(max_value - 1)