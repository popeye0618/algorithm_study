#BABBA
#내 풀이
#dp에 i번 눌렀을 때의 길이가 들어간다.
#규칙은 피보나치 수열과 같다.
#A는 이전 문자의 B의 수 만큼이 있고,
#B는 이전 문자의 길이만큼 있다.

n = int(input())

if n == 1:
  print('0 1')
else:
  dp = [0] * (n + 1)
  dp[1] = 1
  
  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  
  print(dp[n - 1], dp[n])