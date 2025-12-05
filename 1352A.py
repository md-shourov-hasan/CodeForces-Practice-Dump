t = int(input())

for _ in range(t):
  result = []
  k = 0
  number = input()

  length = len(number)
    
  for j in range(length):
    if number[j] != "0":
      k += 1
      result.append(number[j] + "0"*(length - 1 - j))
  print(k)
  print(*result)




