#RGB거리
#내 풀이
#dp에 빨간색을 고른 경우, 파란색을 고른 경우, 초록색을 고른 경우를 모두 넣는다.

n = int(input())
house = []
for _ in range(n):
  house.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)]
for i in range(3):
    dp[0][i] = house[0][i]

for i in range(1, n):
  for j in range(3):
    #red
    if j == 0:
      dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][j]
    #green
    elif j == 1:
      dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + house[i][j]
    #blue
    elif j == 2:
      dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + house[i][j]

print(min(dp[n - 1]))