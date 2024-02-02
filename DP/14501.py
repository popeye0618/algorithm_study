#퇴사
#내 풀이
#dp[i]에는 i일에서의 최대 금액
#거꾸로 탐색해서 시간이 넘지 않는 경우에
#상담을 하느냐 안하느냐를 고려

n = int(input())
time = []
price = []
for _ in range(n):
  t, p = map(int, input().split())
  time.append(t)
  price.append(p)

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
  if i + time[i] <= n:
    dp[i] = max(dp[i + 1], dp[i + time[i]] + price[i])
  else:
    dp[i] = dp[i + 1]
print(dp[0])