#나무 자르기(실버 2)
#내 풀이
#이분탐색으로 얼만큼의 나무를 자를지 정하고
#얻은 나무의 길이를 계산해서 mid값 조정

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

left = 1
right = trees[-1]

result = 0
while left <= right:
  mid = (left + right) // 2
  total = 0
  for tree in trees:
    if tree > mid:
      total += (tree - mid)

  if total >= m:
    result = mid
    left = mid + 1
  else:
    right = mid - 1

print(result)