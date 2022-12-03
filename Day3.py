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
  while True:
    try:
      line1 = input()
      line2 = input()
      line3 = input()
      common_char = ''.join(set(line1).intersection(set(line2).intersection(line3)))
      common_char = common_char.strip()
      if (common_char.islower()):
        prioritySum += (ord(common_char) - 96)
      else:
        prioritySum += (ord(common_char) - 38)
    except EOFError:
      break
  print(prioritySum)

if __name__ == "__main__":
  #firstStar()
  secondStar()