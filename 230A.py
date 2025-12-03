x_array = []
y_array = []

s , n = map(int,input().split())
win = 0

for _ in range(n):
  x, y = map(int,input().split())
  x_array.append(x)
  y_array.append(y)

for i in range(n - 1):
  for j in range(n - i - 1):

    if x_array[j] == x_array[j+1]:
      y_array[j], y_array[j+1] = y_array[j+1], y_array[j]
      x_array[j], x_array[j+1] = x_array[j+1], x_array[j]

    elif x_array[j] > x_array[j+1]:
      x_array[j], x_array[j+1] = x_array[j+1], x_array[j]
      y_array[j], y_array[j+1] = y_array[j+1], y_array[j]

for i in range(n):
  if x_array[i] < s:
    s += y_array[i]
    win += 1


if win == n:
  print("YES")

else:
  print("NO")

