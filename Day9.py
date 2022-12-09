def firstStar(lines):
  coord = set((0, 0))
  head = [0, 0]
  tail = [0, 0]
  for line in lines:
    direction, steps = line.split(" ")
    steps = int(steps)
    while steps > 0:
      # check if head and tail are more than 1 unit apart
      if direction == 'R':
        head[0] += 1
      elif direction == 'L':
        head[0] -= 1
      elif direction == 'U':
        head[1] += 1
      elif direction == 'D':
        head[1] -= 1
      print("HEAD COORD: ", head)
      if head[0] != tail[0] and head[1] != tail[1]: # diagonal
        if abs(head[0] - tail[0]) > abs(head[1] - tail[1]): #x diff more than y diff
          tail[0] = head[0] - 1 if head[0] > tail[0] else head[0] + 1
          tail[1] = head[1]
        else: # y diff more than x diff
          tail[1] = head[1] - 1 if head[1] > tail[1] else head[1] + 1
          tail[0] = head[0]
      elif abs(head[0] - tail[0] > 1) or abs(head[1] - tail[1] > 1): # simple 2 diff
        if head[0] == tail[0]: # in the same row
          tail[1] = head[1] - 1 if head[1] > tail[1] else head[1] + 1
        else: # in the same col
          tail[0] = head[0] - 1 if head[0] > tail[0] else head[0] + 1
      coord.add(tuple(tail))
      print("TAIL COORD: ", tail)
      steps -= 1
  print("FIRST STAR: ", len(coord) - 1)

def firstStar2(lines):
  rope = [0 + 0j] * 2
  moves = {"L": -1j, "R": 1j, "U": 1, "D": -1}
  hist = set(rope)

  for line in lines:
    direction, step = line.split(" ")
    step = int(step)
    for _ in range(step):
      rope[0] += moves[direction]
      for i in range(1, len(rope)):
        if abs((d := rope[i - 1] - rope[i])) >= 2:
          move = int(d.real / 2) + 1j * int(d.imag / 2)
          rope[i] = rope[i - 1] - move 
      hist.add(rope[-1])
  print("FIRST STAR TAIL COORD: ", len(hist))
def secondStar(lines):
  rope = [0 + 0j] * 10
  moves = {"L": -1j, "R": 1j, "U": 1, "D": -1}
  hist = set(rope)

  for line in lines:
    direction, step = line.split(" ")
    step = int(step)
    for _ in range(step):
      rope[0] += moves[direction]
      for i in range(1, len(rope)):
        if abs((d := rope[i - 1] - rope[i])) >= 2:
          move = int(d.real / 2) + 1j * int(d.imag / 2)
          rope[i] = rope[i - 1] - move 
      hist.add(rope[-1])
  print("SECOND STAR TAIL COORD: ", len(hist))

if __name__ == "__main__":
  with open("inputs/day_9_input.txt") as f:
    lines = f.readlines()
  #firstStar(lines) 
  firstStar2(lines)
  secondStar(lines)