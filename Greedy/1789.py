#수들의 합(실버 5)
#내 풀이
#서로 다른 자연수의 합으로 S를 만드는 경우 중 최대 값을 만드는 경우는
#작은 수들로 이뤄지는 것이 합리적이다.

s = int(input())
val = 1
ans = 0
while s > 0:
  if val > s:
    break
  s -= val
  val += 1
  ans += 1

print(ans)