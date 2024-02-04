#합분해(골드 5)
#내 풀이
#DP이용 (조합의 맨 앞자리 수를 기준으로)
#나머지연산 까먹지 말자!!

n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k + 1):
  for j in range(n + 1):
    if i == 1:
      dp[1][n] = 1
    else:
      dp[i][j] = sum(dp[i - 1][j:]) % 1000000000

print(sum(dp[k]) % 1000000000)