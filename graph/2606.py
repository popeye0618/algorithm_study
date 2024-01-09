#바이러스(실버 3)
#내 풀이
#아무거나 사용해서 풀어도 풀릴 것 같은데
#서로소 집합인 것 같으니 유니온 - 파인드 알고리즘 연습을 해보자

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n = int(input())
m = int(input())
parent = [x for x in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

for i in range(1, n + 1):
  find_parent(parent, i)

count = 0
for x in parent:
  if x == 1:
    count += 1

print(count - 1)