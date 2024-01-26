#용돈 관리(실버 2)
#내 풀이
#최소는 용돈 중에 가장 큰 수
#최대는 용돈의 합
#mid라는 금액에 대한 인출 횟수를 세서 m번인지 확인
#최소 인출횟수를 위해 cnt를 1로 설정
#최소 금액을 위해 right를 줄일 때, result 저장

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

left = max(arr)
right = sum(arr)

result = right
while left <= right:
  mid = (left + right) // 2
  tmp = mid
  cnt = 1

  for x in arr:
    if tmp < x:
      tmp = mid
      cnt += 1
    tmp -= x

  if cnt <= m:
    right = mid - 1
    result = mid
  else:
    left = mid + 1

print(result)