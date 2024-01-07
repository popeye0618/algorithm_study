#회의실 배정(실버 1)
#내 풀이
#우선 시작시간을 기준으로 오름차순 정렬을 시킨다.
#시작시간이 같다면 종료시간을 기준으로 오름차순 정렬한다.
#끝나는 시간을 비교하면서 시작시간이 끝나는 시간을 넘지 않는 선에서
#끝나는 시간이 가장 빠른 회의를 선택한다.

n = int(input())
meeting = []
for _ in range(n):
  meeting.append(tuple(map(int, input().split())))

meeting.sort(key = lambda x : (x[0], x[1]))
answer = 1
end_time = meeting[0][1]


for i in range(1, n):
  if meeting[i][0] >= end_time:
    end_time = meeting[i][1]
    answer += 1
  elif meeting[i][1] < end_time:
    end_time = meeting[i][1]

print(answer)