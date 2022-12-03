from sys import stdin

def firstStar():
  prioritySum = 0
  for line in stdin:
    size = len(line)
    half = int(size / 2)
    firstHalf = line[:half] 
    secondHalf = line[half:]
    common_char =''.join(set(firstHalf).intersection(secondHalf))
    if (common_char.islower()):
      prioritySum += (ord(common_char) - 96)
    else:
      prioritySum += (ord(common_char) - 38)
  print(prioritySum)

def secondStar():
  prioritySum = 0
  lines = [line for line in stdin][:3]
  print(lines)
  for line in stdin:
    if count < 3:
      lines[count] = line
      count += 1
    else:
      count = 0
      common_char = ''.join(set(lines[0]).intersection(set(lines[1]).intersection(lines[2])))
      common_char = common_char.strip()
      if (common_char.islower()):
        prioritySum += (ord(common_char) - 96)
      else:
        prioritySum += (ord(common_char) - 38)
      
  print(prioritySum)

if __name__ == "__main__":
  #firstStar()
  secondStar()