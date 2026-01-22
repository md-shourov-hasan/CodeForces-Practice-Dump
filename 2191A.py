test = int(input())
for _ in range(test):
  length = int(input())
  arr = list(map(int, input().split()))

  numbers = [[arr[i], "RED" if i % 2 == 0 else "BLUE"] for i in range(length)]


  new_number = sorted(numbers)


  Flag = False


  for j in range(length - 1):

    if (new_number[j][1] == new_number[j+1][1]):
      Flag = True
      break


  if Flag:
    print("NO")
  else:
    print("YES")