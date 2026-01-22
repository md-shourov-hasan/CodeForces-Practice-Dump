import bisect
import sys
input = lambda: sys.stdin.readline()

shopNumber = int(input())

priceArray = list(map(int,input().split()))
priceArray.sort()

Days = int(input())

for i in range(Days):
  coinSpent = int(input())

  canSpend = bisect.bisect_right(priceArray, coinSpent)

  

  print(canSpend)
