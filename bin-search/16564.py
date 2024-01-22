#히오스 프로게이머(실버 1)
#내 풀이
#최소 레벨을 가장 크게 만드는 것이 목표
#left를 최소 레벨, right를 경험치를 사용해 만들 수 있는 최대 레벨
#mid값을 조절하며 만들 수 있는 지 확인

n, k = map(int, input().split())
levels = []
for _ in range(n):
  levels.append(int(input()))

levels.sort()
left = levels[0]
right = levels[-1] + k

result = 0
while left <= right:
  mid = (left + right) // 2
  exp = 0
  
  for level in levels:
    if mid - level > 0:
      exp += mid - level
    
  if exp <= k:
    result = mid
    left = mid + 1
  else:
    right = mid - 1

print(result)