#연구소(골드 4)
#내 풀이
#벽을 반드시 3개를 세워야 한다. 따라서 모든 곳에 벽을 쳐보고 바이러스를 퍼뜨려서
#안전영역이 최대인 경우를 출력한다.
#백트래킹을 사용하여 벽을 세운다.
#백트래킹을 이용하면 자동으로 세웠다가 풀렸다가 하기때문에 모든 경우를 다 해볼 수 있다.

from collections import deque
import copy

def bfs():
  global answer
  field = copy.deepcopy(graph)
  queue = deque()
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2:
        queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0:
        field[nx][ny] = 2
        queue.append((nx, ny))
  cnt = 0
  for i in range(n):
    for j in range(m):
      if field[i][j] == 0:
        cnt += 1
  answer = max(answer, cnt)

def wall(cnt):
  if cnt == 3:
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if cnt < 3 and graph[i][j] == 0:
        graph[i][j] = 1
        wall(cnt + 1)
        graph[i][j] = 0

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
wall(0)
print(answer)