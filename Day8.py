import numpy as np

def firstStar(lines):
  graph = [list(map(int, list(line))) for line in lines]
  r = len(graph)
  c = len(graph[0])

  graph = np.array(graph)

  visible = 0

  for i in range(r):
    for j in range(c):
      k = graph[i, j]

      if j == 0 or np.amax(graph[i, :j]) < k:
        visible += 1
      elif j == c - 1 or np.amax(graph[i, (j+1):]) < k:
        visible += 1
      elif i == 0 or np.amax(graph[:i, j]) < k:
        visible += 1
      elif i == r - 1 or np.amax(graph[(i+1):, j]) < k:
        visible += 1
  print("FIRST STAR: ", visible)



def secondStar(lines):
  graph = [list(map(int, list(line))) for line in lines]
  r = len(graph)
  c = len(graph[0])
  ans = 0
  dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]

  for i in range(r):
    for j in range(c):
      k = graph[i][j]
      score = 1

      for dx, dy in dd:
        ii, jj = i + dx, j + dy
        dist = 0

        while (0 <= ii < r and 0 <= jj < c) and graph[ii][jj] < k:
          dist += 1
          ii += dx 
          jj += dy

          if (0 <= ii < r and 0 <= jj < c) and graph[ii][jj] >= k:
            dist += 1
        
        score *= dist
      ans = max(ans, score)
  print("SECOND STAR: ", ans)

if __name__ == "__main__":
  with open("inputs/day_8_input.txt") as f:
    lines = f.read().strip().split()
  firstStar(lines) 
  secondStar(lines)