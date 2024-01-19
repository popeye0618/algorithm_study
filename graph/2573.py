#빙산(골드 4)
#내 풀이
#BFS를 사용해서 빙산을 녹이기도 하고, 빙산이 몇 개인지 세준다.
#즉시 녹이는 것보다 따로 저장해두고 그 후에 한 번에 녹인다.
#즉시 녹이면서 가면 빙산이 0으로 바뀌고 다른 지점에 영향을 줄 수 있다.
#따라서 처리 순서상 얼만큼 녹을지 저장해두고, 한 번에 녹이는 것이 좋다.
#그 후에는 bfs를 돌린 횟수만큼 빙산이 존재하므로 이 횟수로 종료 조건을 설정한다.

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
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
        if graph[nx][ny] == 0:
          melt[x][y] += 1
        else:
            visited[nx][ny] = True
            queue.append((nx, ny))

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while True:
  melt = [[0 for _ in range(m)] for _ in range(n)]
  visited = [[False for _ in range(m)] for _ in range(n)]
  cnt = 0

  #빙산 개수와 녹일 정보 얻기
  for i in range(n):
    for j in range(m):
      if graph[i][j] > 0 and not visited[i][j]:
        bfs(i, j)
        cnt += 1
  #빙산 녹이기
  for i in range(n):
    for j in range(m):
      if melt[i][j] > 0:
        graph[i][j] = max(graph[i][j] - melt[i][j], 0)
  
  if cnt == 0:
    print(0)
    break
  elif cnt > 1:
    print(time)
    break
  time += 1