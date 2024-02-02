#이친수
#내 풀이
#0붙는건 i - 1개, 1붙는건 i - 2개

n = int(input())
dp = [1] * (n + 1)

for i in range(3, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])