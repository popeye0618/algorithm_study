#과자 나눠주기(실버 2)
#내 풀이
#과자의 길이를 합칠 수 없다.
#필요한 조건은 과자의 길이가 조카의 수보다 작을 경우 불가능
#과자를 자르는 동작을 이분탐색으로 구현하고
#자른 후에 과자가 몇 개인지, 조카의 수보다 많거나 같으면 저장 후 left 증가

n, k = map(int, input().split())
snacks = list(map(int, input().split()))

result = 0
if sum(snacks) < n:
  print(0)
else:
  snacks.sort()
  left = 1
  right = snacks[-1]
  while left <= right:
    mid = (left + right) // 2
    cnt = 0
  
    for i in range(len(snacks)):
      cnt += snacks[i] // mid
  
    if cnt >= n:
      result = mid
      left = mid + 1
    else:
      right = mid - 1

  print(result)