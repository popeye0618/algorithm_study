#랜선 자르기(실버 2)
#내 풀이
#랜선의 최대 길이는 모든 랜선을 더한 값을 n으로 나누면 그게 최대이다.
#하지만 랜선의 길이가 각각 다르기에 이분탐색으로 최적의 값을 찾는다.

k, n = map(int, input().split())
cables = []
for _ in range(k):
  cables.append(int(input()))

cables.sort()

left = 1
right = sum(cables) // n

result = 0
while left <= right:
  mid = (left + right) // 2
  cnt = 0

  for cable in cables:
    cnt += cable // mid

  if cnt >= n:
    result = mid
    left = mid + 1
  else:
    right = mid - 1

print(result)