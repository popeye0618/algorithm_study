#안전 영역
#내 풀이

from collections import deque

def bfs(x, y, h):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
        visited[nx][ny] = True
        queue.append((nx, ny))

n = int(input())
graph = []
max_value = 0
for i in range(n):
  graph.append(list(map(int, input().split())))
  max_value = max(max_value, max(graph[i]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 1
for height in range(1, max_value + 1):
  visited = [[False for _ in range(n)] for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if graph[i][j] > height and not visited[i][j]:
        bfs(i, j, height)
        cnt += 1
  answer = max(answer, cnt)

print(answer)