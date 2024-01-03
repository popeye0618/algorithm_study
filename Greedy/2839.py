#설탕 배달(실버 4)
#내 풀이
#5kg봉지를 많이 가져가는 것이 최소가 될 수 있다.

n = int(input())
result = 0

while True:
  if n == 0:
    print(result)
    break
  elif n < 0:
    print(-1)
    break
  if n % 5 == 0:
    result += n // 5
    n %= 5
  else:
    n -= 3
    result += 1
