#숫자 카드(실버 5)
#내 풀이
#그냥 수 찾기랑 같은 문제..

n = int(input())
num = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

answer = []
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
    answer.append(1)
  else:
    answer.append(0)

print(' '.join(map(str, answer)))