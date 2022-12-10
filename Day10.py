from collections import deque

def firstStar(lines):
  X = 1
  cycle = deque()
  cycle.append((1, 0))
  curr = 0
  for line in lines:
    if 'noop' in line:
      cycle.append((curr + 1, 0)) # (time, add)
      curr += 1
    else: 
      _, val = line.split(" ")
      val = int(val)
      cycle.append((curr + 2, val))
      curr += 2
  
  res = 0
  count = 0
  while len(cycle) > 0:
    while len(cycle) > 0 and cycle[0][0] <= count:
      _, val = cycle.popleft()
      X += val 
    count += 1
    if count == 20 or (count - 20) % 40 == 0:
      res += count * (X)


  #print("CYCLE: ", cycle)
  print("FIRST STAR: ", res) 

def _signals(lines, cycle=0, register=1):
  for line in lines:
    if line.startswith("addx "):
      cycle += 2
      register += int(line[5:])
    else:
      cycle += 1
    yield cycle, register

def secondStar(lines):
  cycle, register, last_register = 0, 1, 1
  signals = _signals(lines)
  result = []
  for row in range(6):
    line = ""
    for col in range(40):
      while cycle <= 40 * row + col:
        last_register = register
        cycle, register = next(signals)
      line += "\u2593" if -1 <= last_register - col <= 1 else "\u2591"
    result.append(line)
  print("SECOND STAR: \n") 
  print("\n".join(result))


if __name__ == "__main__":
  with open("inputs/day_10_input.txt") as f:
    lines = f.readlines()
  firstStar(lines)
  secondStar(lines)