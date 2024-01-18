#단지번호붙이기(실버 1)
#DFS로 풀기
#내 풀이
#스택으로 구현했다. 스택으로 구현하면 bfs랑 구현 방식이 크게 다를게 없다.
#방문가능한 곳 모두 방문하며 cnt를 늘려주고 dfs는 cnt를 리턴한다.
#answer리스트에 있는 개수만큼 단지가 존재하며, 정렬후 하나씩 출력한다.

def dfs(x, y):
  stack = []
  stack.append((x, y))
  visited[x][y] = True
  cnt = 1
  while stack:
    x, y = stack.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][
          ny] == '1':
        stack.append((nx, ny))
        visited[nx][ny] = True
        cnt += 1

  return cnt


n = int(input())
graph = []
for _ in range(n):
  graph.append(input())

visited = [[False for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == '1' and not visited[i][j]:
      answer.append(dfs(i, j))

print(len(answer))
answer.sort()
for i in answer:
  print(i)
