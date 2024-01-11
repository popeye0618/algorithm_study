#유기농 배추(실버 2)
#내 풀이
#저번에 풀었던대로 영역나누기 문제다.

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
        visited[nx][ny] = True
        queue.append((nx, ny))

t = int(input())
while t > 0:
  m, n, k = map(int, input().split())
  graph = [[0 for _ in range(m)] for _ in range(n)]
  visited = [[False for _ in range(m)] for _ in range(n)]
  cnt = 0
  
  for _ in range(k):
    b, a = map(int, input().split())
    graph[a][b] = 1
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1 and not visited[i][j]:
        cnt += 1
        bfs(i, j)
  print(cnt)
  t -= 1