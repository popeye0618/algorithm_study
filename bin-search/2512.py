#예산(실버 2)
#내 풀이
#mid로 예산측정해보고 총 예산보다 작으면 mid 증가

n = int(input())
req = list(map(int, input().split()))
m = int(input())

req.sort()
left = 1
right = req[-1]

result = 0
while left <= right:
  mid = (left + right) // 2
  total = 0

  for x in req:
    total += x if x <= mid else mid

  if total <= m:
    result = mid
    left = mid + 1
  else:
    right = mid - 1

print(result)