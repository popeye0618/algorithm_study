#로프(실버 4)
#내 풀이
#우선 병렬로 연결하지 않았을 때 최대 중량은 max값
#병렬로 연결할 경우의 최대 중량은 가장 작은 수 * 그 수보다 크거나 같은 수의 개수
#최종적으로 비교해본다.

import sys
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
  rope.append(int(input()))

rope.sort()
answer = rope[-1]

for i in range(len(rope)):
  t = len(rope) - i
  answer = max(answer, rope[i] * t)

print(answer)
