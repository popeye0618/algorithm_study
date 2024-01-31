#리그오브레전설(실버 2)
#내 풀이
#dp 리스트에는 조합의 수가 들어간다.
#따라서 dp[i]는 i초에서 누를 수 있는 조합의 수.
#m초 전에 경우의 수는 무조건 1개 (AA...)
#m초 이후부터는 (i - 1초에서 A를 누른 경우) + (i - m초에서 B를 누른 경우) 이다.

n, m = map(int,input().split())
dp = [0] * (n + 1)

for i in range(n + 1):
  if i < m:
    dp[i] = 1
  else:
    dp[i] = (dp[i - 1] + dp[i - m]) % 1000000007

print(dp[n])