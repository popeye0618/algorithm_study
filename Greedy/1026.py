#보물(실버 4)
#내 풀이
#최소 값을 만들어야하므로 a는 오름차순, b는 내림차순 정렬하고
#같은 인덱스끼리 그냥 곱해주면 된다.

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

answer = 0
for i in range(n):
  answer += a[i] * b[i]
print(answer)