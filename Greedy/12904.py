#A와 B(골드 5)
#내 풀이
#거꾸로 T를 이용해서 S를 만들면 된다.
#수행도 반대로 하면 되는데
#A를 만나면 A제거
#B를 만나면 B제거 후 뒤집기

s = input()
t = input()

while True:
  if t == s:
    print(1)
    break
  if len(s) > len(t):
    print(0)
    break
  if t[-1] == 'A':
    t = t[: -1]
  else:
    t = t[: -1]
    t = t[:: -1]