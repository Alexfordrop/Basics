daily = [0, 1, 5, 0, 8, 0, 0, 5, 3, 0, 1, 0]


for i in daily:

  if i != 0:
    return True

def things(number, time)
  pass

s = input()
ans = ''
anscnt = 0
for i in range(len(s)):
  nowcnt = 0
  for j in range(len(s)):
    if s[i] == s[j]:
      nowcnt += 1
  if nowcnt > anscnt:
    ans = s[i]
    anscnt = nowcnt
    
print(ans)
