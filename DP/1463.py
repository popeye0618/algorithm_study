#1로 만들기(실버 3)
#내 풀이
#dp[i]에는 i에서의 최소 연산 횟수

n = int(input())
dp = [0] * (n + 1)

if n >= 2:
  dp[2] = 1
if n >= 3:
  dp[3] = 1
for i in range(4, n + 1):
  dp[i] = dp[i - 1] + 1

  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp)