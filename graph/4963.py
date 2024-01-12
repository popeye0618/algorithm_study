#섬의 개수
#이것도 영역나누기 문제

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()
    for i in range(8):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
        visited[nx][ny] = True
        queue.append((nx, ny))

while True:
  m, n = map(int, input().split())
  if n == 0 and m == 0:
    break

  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))
  visited = [[False] * m for _ in range(n)]
  dx = [-1, 1, 0, 0, -1, -1, 1, 1]
  dy = [0, 0, -1, 1, -1, 1, -1, 1]
  
  answer = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1 and not visited[i][j]:
        bfs(i, j)
        answer += 1

  print(answer)