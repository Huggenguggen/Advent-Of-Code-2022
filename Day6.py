def firstStar(line):
  chars = set()
  chars.add(line[0])
  l = 0
  r = 1
  while len(chars) < 4:
    if line[r] not in chars:
      chars.add(line[r])
      r += 1
    else:
      if line[l] != line[r]:  
        chars.remove(line[l])
      else:
        r += 1
      l += 1
  print("packet count: ", r)

def secondStar(line):
  chars = set()
  chars.add(line[0])
  l = 0
  r = 1
  while len(chars) < 14:
    if line[r] not in chars:
      chars.add(line[r])
      r += 1
    else:
      if line[l] != line[r]:  
        chars.remove(line[l])
      else:
        r += 1
      l += 1
  print("message count: ", r)


if __name__ == "__main__":
  with open("inputs/day_6_input.txt") as f:
    lines = f.readlines()
  firstStar(lines[0]) 
  secondStar(lines[0])