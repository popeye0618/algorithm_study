#주유소(실버 3)
#내 풀이
#낮은 가격으로 많은 거리를 가는 것이 최소 가격으로 갈 수 있는 방법일 것이다.
#처음부터 시작해서 가격을 저장해놓고, 다음 지점에 도착했을 때
#도착 지점의 가격이 높다면 원래 가격으로 주유하고
#낮다면 가격을 갱신하고 그 가격으로 주유한다.

import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

current_price = price[0]
answer = 0
for i in range(len(distance)):
  current_price = min(current_price, price[i])
  answer += current_price * distance[i]
print(answer)