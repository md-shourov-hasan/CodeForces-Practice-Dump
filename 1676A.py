t = int(input())

for _ in range(t):
  total = 0
  total2 = 0

  ticket = str(input())

  for i in range(0,3):
    total += int(ticket[i])

  for j in range(3,6):
    total2 += int(ticket[j])

  if total == total2:
    print("YES")
  else:
    print("NO")