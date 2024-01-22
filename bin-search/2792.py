#보석 상자(실버 1)
#내 풀이
#보석을 몇 개로 나눌지 최대의 값을 mid로 결정할 것이다.
#따라서 mid로 계산해보고, 학생 수보다 크면 mid를 낮춘다.
#mid작아지면 학생수가 커짐

n, m = map(int, input().split())
jewels = []
for _ in range(m):
  jewels.append(int(input()))

jewels.sort()
left = 1
right = jewels[-1]

result = 0
while left <= right:
  mid = (left + right) // 2
  cnt = 0
  
  for jewel in jewels:
    if jewel % mid != 0:
      cnt += 1
    cnt += jewel // mid

  if cnt <= n:
    result = mid
    right = mid - 1
  else:
    left = mid + 1

print(result)