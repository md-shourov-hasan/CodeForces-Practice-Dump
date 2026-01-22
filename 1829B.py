import sys
input = lambda: sys.stdin.readline()

t = int(input())

for _ in range(t):
  
  space = 0
  maxspace = 0

  length = int(input())
  myarr = list(map(int,input().split()))

  i = 0
  while i < length:

    if myarr[i] == 0:
      space += 1

    elif myarr[i] == 1:
      if space > maxspace:
        maxspace = space

      space = 0
    
    i += 1

  if space > maxspace:
    maxspace = space

  print(maxspace)





