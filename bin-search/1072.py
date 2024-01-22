#게임(실버 3)
#내 풀이
#앞으로의 게임은 모두 승리이기 때문에 z가 99보다 크면 승률은 바뀌지 않는다.
#최소 1판을 더 하므로 left = 1, x판 더 하면 반드시 바뀌므로 right = x로 설정
#판수로 이분탐색을 해서 승률이 바뀌면 결과 저장 후 판수 감소

x, y = map(int, input().split())
z = (y * 100) // x

def binary_search(z, x, y):
  if z >= 99:
    return -1
  left = 1
  right = x
  ans = 0
  while left <= right:
    mid = (left + right) // 2
    if ((y + mid) * 100) // (x + mid) > z:
      ans = mid
      right = mid - 1
    else:
      left = mid + 1
  return ans

print(binary_search(z, x, y))