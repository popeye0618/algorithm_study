#맥주 마시면서 걸어가기
#내 풀이
#문제를 읽어보면 결국 한 지점으로부터 다른 지점까지의 거리가(맨해튼 거리)
#1000 이하이면 갈 수 있다는 뜻이다.
#따라서 현재 위치부터 거리가 1000 이하인 곳을 가보는 bfs문제라는걸 알 수 있다.

from collections import deque

def distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(home):
  queue = deque()
  queue.append((home))
  visited.add(home)

  while queue:
    now = queue.popleft()
    if now == dest:
      return 'happy'
    for t in graph:
      if t not in visited and distance(t, now) <= 1000:
        queue.append(t)
        visited.add(t)
        
  return 'sad'
t = int(input())
for _ in range(t):
  n = int(input())
  home = tuple(map(int, input().split()))

  graph = []
  for _ in range(n):
    graph.append(tuple(map(int, input().split())))
  dest = tuple(map(int, input().split()))
  graph.append(dest)
  visited = set()
  
  print(bfs(home))