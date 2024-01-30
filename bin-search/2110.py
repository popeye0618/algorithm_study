#공유기 설치(골드 4)
#내 풀이
#두 공유기 사이의 거리를 mid로 유도
#최대거리이므로 left 늘려줄 때 result 저장
#첫 지점에 공유기를 설치하고 시작하는게 좋은 아이디어
#첫 지점부터 현재 위치까지의 거리가 mid가 넘어가는 경우 공유기 설치

n, m = map(int, input().split())
home = []
for _ in range(n):
  home.append(int(input()))

home.sort()
left = 1
right = home[-1] - home[0]

result = 0
while left <= right:
  mid = (left + right) // 2
  cnt = 1
  last = home[0]

  for x in home[1:]:
    if x - last >= mid:
      cnt += 1
      last = x

  if cnt >= m:
    result = mid
    left = mid + 1
  else:
    right = mid - 1

print(result)