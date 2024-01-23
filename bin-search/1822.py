#차집합(실버 4)
#내 풀이
#이것도 그냥 간단한 이분탐색

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = set()
a.sort()

for x in b:
  left = 0
  right = n - 1
  while left <= right:
    mid = (left + right) // 2

    if x == a[mid]:
      tmp.add(a[mid])
      break
    elif x > a[mid]:
      left = mid + 1
    else:
      right = mid - 1

answer = [x for x in a if x not in tmp]
if len(answer) == 0:
  print(0)
else:
  print(len(answer))
  answer.sort()
  print(' '.join(map(str, answer)))

#파이썬이 사기인 이유
n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

answer = a - b

if len(answer) == 0:
  print(0)
else:
  print(len(answer))
  for x in sorted(answer):
    print(x, end=' ')