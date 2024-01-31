#타일 장식물
#내 풀이
#가장 큰 타일 넓이 * 2 + (가장 큰 타일넓이 + 이전 타일 넓이) * 2

n = int(input())
dp = [0] * (n + 1)
if n >= 1:
  dp[1] = 1
if n >= 2:
  dp[2] = 1
for i in range(3, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2]

answer = dp[n] * 2 + (dp[n] + dp[n - 1]) * 2
print(answer)