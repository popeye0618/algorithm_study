#ATM(실버 4)
#내 풀이
#그냥 정렬해서 더하면 될 것 같다.
#그리디인 이유는 그 순간에 가장 시간이 적게 걸리는 사람을 고르면 되기 때문
#1000명까지라 이중 for문 충분히 가능

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
for i in range(n):
  for j in range(i + 1):
    result += arr[j]

print(result)