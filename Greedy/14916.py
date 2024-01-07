#거스름돈(실버 5)
#내 풀이
#저번에 풀었던 설탕문제와 똑같은 것 같다.

n = int(input())

answer = 0
while True:
  if n % 5 == 0:
    answer += n // 5
    n %= 5
  if n == 0:
    print(answer)
    break
  if n < 0:
    print(-1)
    break
  n -= 2
  answer += 1