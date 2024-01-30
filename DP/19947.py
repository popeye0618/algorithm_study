#투자의 귀재
#내 풀이
#dp[i]에 들어갈 값은 i년에 가지고 있는 금액의 최대값

n, m = map(int, input().split())
dp = [0] * (m + 1)
dp[0] = n

for i in range(1, m + 1):
  dp[i] = dp[i - 1] + dp[i - 1] * 5 // 100

  if i >= 3:
    dp[i] = max(dp[i], dp[i - 3] + dp[i - 3] * 20 // 100 )

  if i >= 5:
    dp[i] = max(dp[i], dp[i - 5] + dp[i - 5] * 35 // 100 )

print(dp[m])