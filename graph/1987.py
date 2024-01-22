#알파벳(골드 4)
#내 풀이
#dfs문제같고, 지금까지 지나왔던 알파벳을 저장해야한다.
#이 문제가 현재 상황을 저장해놓고, 이어가는 방식이다.
#모든 경우가 확인할 문자열을 공유하지 않도록 잘 분리하는 것이 중요하다.
#저번엔 스택으로, 이번엔 재귀로 풀었다.
#다 풀고 생각해보니 방문 배열이 필요가 없을 것 같다.
#어차피 한 번 지나가면 문자열이 저장되므로, 다시 방문할 일이 없다.

def dfs(x, y, depth, string):
  global answer
  answer = max(answer, depth)
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] not in string:
      dfs(nx, ny, depth + 1, string + graph[nx][ny])

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
dfs(0, 0, 1, graph[0][0])
print(answer)