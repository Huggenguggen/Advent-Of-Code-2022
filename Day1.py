from sys import stdin
from heapq import heapify, heappush, heappop

def mostCalories():
  minHeap = [0, 0, 0]
  heapify(minHeap)
  temp = 0
  for line in stdin:
    if line == '\n':
      third_highest = heappop(minHeap)
      third_highest = third_highest if third_highest > temp else temp
      heappush(minHeap, third_highest)
      temp = 0
    else:
      temp += int(line)
    


  print("MINHEAP is: ", minHeap)
  print("TOTAL OF TOP 3 is: ", sum(minHeap))

if __name__ == "__main__":
  mostCalories()

