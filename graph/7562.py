#나이트의 이동(실버 1)
#내 풀이
#이것도 8방향 bfs로 풀면 된다.

from collections import deque

def bfs():
  queue = deque()
  queue.append(start)
  visited[start[0]][start[1]] = 1

  while queue:
    x, y = queue.popleft()
    if x == dest[0] and y == dest[1]:
      print(visited[x][y] - 1)
      break
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))

t = int(input())
for _ in range(t):
  n = int(input())
  visited = [[0 for _ in range(n)] for _ in range(n)]
  start = tuple(map(int, input().split()))
  dest = tuple(map(int, input().split()))

  dx = [-2, -2, 2, 2, -1, -1, 1, 1]
  dy = [-1, 1, -1, 1, -2, 2, -2, 2]
  bfs()