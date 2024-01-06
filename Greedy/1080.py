#행렬(실버 1)
#내 풀이
#아이디어가 안떠오른다.
#그냥 탐색하면서 a랑 b랑 다르면 다른 점 기준으로 x + 2, y + 2까지 뒤집어본다.
#그리디적인 요소는 a와 b의 같은 위치의 원소가 다르면 뒤집는 연산을 수행한다는 점이며
#정당성은 a와 b가 달라서 뒤집은 경우 해당 위치의 원소는 다시 방문하지 않고,
#0과 1밖에 존재하지 않으므로 반드시 행렬 b와 같아질 수 있다.

def flip(x, y):
  for i in range(3):
    for j in range(3):
      if mat_a[x + i][y + j] == 0:
        mat_a[x + i][y + j] = 1
      else:
        mat_a[x + i][y + j] = 0
          
n, m = map(int, input().split())
mat_a = []
mat_b = []

for _ in range(n):
  mat_a.append(list(map(int, input())))
for _ in range(n):
  mat_b.append(list(map(int, input())))

answer = 0
for x in range(n):
  for y in range(m):
    if mat_a[x][y] != mat_b[x][y]:
      if x + 2 < n and y + 2 < m:
        flip(x, y)
        answer += 1

if mat_a != mat_b:
  print(-1)
else:
  print(answer)