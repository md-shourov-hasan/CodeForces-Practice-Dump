t = int(input())

for _ in range(t):
  number = str(input())
  total = 0
  for i in range(2):
    total += int(number[i])
  print(total)