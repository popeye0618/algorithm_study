#입국 심사(골드 5)
#내 풀이
#걸리는 시간을 mid로 나오게 할 예정
#따라서 mid시간동안 입국심사대에서 걸리는 시간으로 나눠줌
#해서 mid시간동안 몇 명이 통과할 수 있는지 검사
#m명 이상이면 결과 저장하고, 시간을 줄여봄

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort()

left = 1
right = arr[-1] * m

result = 0
while left <= right:
  mid = (left + right) // 2
  total = 0
  
  for time in arr:
    total += mid // time

  if total >= m:
    result = mid
    right = mid - 1

  else:
    left = mid + 1

print(result)