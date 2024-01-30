#계단오르기(실버 3)
#내 풀이
#두 계단 전을 밟느냐, 한 계단 전을 밟느냐 (이번 계단은 반드시 밟음)
#현재 계단은 반드시 밟는다고 가정(i가 증가할 때마다 i가 마지막 계단이라고 생각하는 것)

n = int(input())
stair = [0]
for _ in range(n):
  stair.append(int(input()))

dp = [0] * (n + 1)
if n >= 1:
  dp[1] = stair[0] + stair[1]
if n >= 2:
  dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n + 1):
  dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[n])