#수 찾기(실버 4)
#내 풀이
#이분 탐색으로 존재하는지 여부를 확인한다.

n = int(input())
num = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

num.sort()
for x in req:
  left = 0
  right = len(num) - 1
  flag = False
  while left <= right:
    mid = (left + right) // 2

    if x == num[mid]:
      flag = True
      break
    elif num[mid] > x:
      right = mid - 1
    elif num[mid] < x:
      left = mid + 1
  if flag:
    print(1)
  else:
    print(0)