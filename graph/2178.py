#미로 탐색
#내 풀이
#bfs를 돌리고 visited을 카운트로 생각해서
#마지막에 visited[n-1][m-1]을 출력한다.

from collections import deque

def bfs():
  queue = deque()
  queue.append((0, 0))
  visited[0][0] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == '1':
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(input())

visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bfs()
print(visited[n - 1][m - 1])