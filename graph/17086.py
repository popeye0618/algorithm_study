#아기 상어2(실버 2)
#내 풀이
#방향만 추가해서 bfs를 돌린다
#이 때 visited 리스트는 아기상어와의 거리로 한다.

from collections import deque

def bfs():
  queue = deque()
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))
      

n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
bfs()

max_value = max(max(row) for row in visited)
print(max_value)